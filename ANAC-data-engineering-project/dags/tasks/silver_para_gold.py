# tasks/gold_transform.py

from airflow.decorators import task
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, monotonically_increasing_id, to_date, dayofmonth, month, year, quarter,
    date_format, weekofyear, when, lit, udf
)
from pyspark.sql.types import BooleanType, StringType
import holidays
import os

BASE_DATA_DIR = "/opt/airflow/data"
SILVER_DIR = os.path.join(BASE_DATA_DIR, "silver")
GOLD_DIR   = os.path.join(BASE_DATA_DIR, "gold")


def silver_para_gold():
    print("🚀 Inicializando SparkSession...")
    spark = SparkSession.builder.appName("ANAC - Camada Gold").getOrCreate()
    spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")

    print("📂 Lendo dados da camada Silver...")
    df = spark.read.parquet(os.path.join(SILVER_DIR, "operacoes_anac_partitioned"))

    # ───── DIMENSÃO EMPRESA ─────
    print("📌 Criando dimensão EMPRESA...")
    dim_empresa = df.select("EMPRESA_SIGLA", "EMPRESA_NOME", "EMPRESA_NACIONALIDADE").dropDuplicates()
    dim_empresa = dim_empresa.withColumn("ID_EMPRESA", monotonically_increasing_id())
    dim_empresa = dim_empresa.select("ID_EMPRESA", "EMPRESA_SIGLA", "EMPRESA_NOME", "EMPRESA_NACIONALIDADE")
    dim_empresa.write.mode("overwrite").parquet(os.path.join(GOLD_DIR, "dim_empresa"))

    # ───── DIMENSÃO AEROPORTO ─────
    print("📌 Criando dimensão AEROPORTO...")
    origem = df.select(
        col("AEROPORTO_DE_ORIGEM_SIGLA").alias("AEROPORTO_ICAO"),
        col("AEROPORTO_DE_ORIGEM_NOME").alias("AEROPORTO_NOME"),
        col("AEROPORTO_DE_ORIGEM_UF").alias("UF"),
        col("AEROPORTO_DE_ORIGEM_REGIAO").alias("REGIAO"),
        col("AEROPORTO_DE_ORIGEM_PAIS").alias("PAIS"),
        col("AEROPORTO_DE_ORIGEM_CONTINENTE").alias("CONTINENTE")
    )
    destino = df.select(
        col("AEROPORTO_DE_DESTINO_SIGLA").alias("AEROPORTO_ICAO"),
        col("AEROPORTO_DE_DESTINO_NOME").alias("AEROPORTO_NOME"),
        col("AEROPORTO_DE_DESTINO_UF").alias("UF"),
        col("AEROPORTO_DE_DESTINO_REGIAO").alias("REGIAO"),
        col("AEROPORTO_DE_DESTINO_PAIS").alias("PAIS"),
        col("AEROPORTO_DE_DESTINO_CONTINENTE").alias("CONTINENTE")
    )
    dim_aeroporto = origem.union(destino).dropDuplicates()
    dim_aeroporto = dim_aeroporto.withColumn("ID_AEROPORTO", monotonically_increasing_id())
    dim_aeroporto = dim_aeroporto.select(
        "ID_AEROPORTO", "AEROPORTO_ICAO", "AEROPORTO_NOME", "UF", "REGIAO", "PAIS", "CONTINENTE"
    )
    dim_aeroporto.write.mode("overwrite").parquet(os.path.join(GOLD_DIR, "dim_aeroporto"))

    # ───── DIMENSÃO TEMPO ─────
    print("📌 Criando dimensão TEMPO...")
    feriados_br = holidays.Brazil()

    @udf(BooleanType())
    def is_feriado(data):
        return data in feriados_br if data else False

    @udf(StringType())
    def estacao_do_ano(data):
        if not data:
            return None
        d, m = data.day, data.month
        if (m == 12 and d >= 21) or m in [1, 2] or (m == 3 and d < 20):
            return "Verão"
        elif (m == 3 and d >= 20) or m in [4, 5] or (m == 6 and d < 21):
            return "Outono"
        elif (m == 6 and d >= 21) or m in [7, 8] or (m == 9 and d < 23):
            return "Inverno"
        else:
            return "Primavera"

    dim_tempo = df.select("DATA").dropDuplicates().withColumn("DATA", to_date("DATA"))
    dim_tempo = dim_tempo.withColumn("DIA", dayofmonth("DATA")) \
                         .withColumn("MES", month("DATA")) \
                         .withColumn("ANO", year("DATA")) \
                         .withColumn("TRIMESTRE", quarter("DATA")) \
                         .withColumn("NOME_DIA_SEMANA", date_format("DATA", "EEEE")) \
                         .withColumn("NOME_MES", date_format("DATA", "MMMM")) \
                         .withColumn("NUM_SEMANA", weekofyear("DATA")) \
                         .withColumn("FIM_DE_SEMANA", when(date_format("DATA", "u").isin("6", "7"), True).otherwise(False)) \
                         .withColumn("FERIADO_BR", is_feriado(col("DATA"))) \
                         .withColumn("ESTACAO", estacao_do_ano(col("DATA"))) \
                         .withColumn("ID_TEMPO", monotonically_increasing_id()) \
                         .select(
                            "ID_TEMPO", "DATA", "DIA", "MES", "NOME_MES", "NUM_SEMANA", "NOME_DIA_SEMANA",
                            "FIM_DE_SEMANA", "FERIADO_BR", "ESTACAO", "TRIMESTRE", "ANO"
                         )
    dim_tempo.write.mode("overwrite").parquet(os.path.join(GOLD_DIR, "dim_tempo"))

    # ───── DIMENSÃO TIPO DE VOO ─────
    print("📌 Criando dimensão TIPO DE VOO...")
    dim_voo = df.select("NATUREZA", "GRUPO_DE_VOO").dropDuplicates()
    dim_voo = dim_voo.withColumn("ID_TIPO_VOO", monotonically_increasing_id())
    dim_voo = dim_voo.select("ID_TIPO_VOO", "NATUREZA", "GRUPO_DE_VOO")
    dim_voo.write.mode("overwrite").parquet(os.path.join(GOLD_DIR, "dim_tipo_voo"))

    # ───── FATO VOO ─────
    print("📊 Criando tabela FATO_VOO...")
    dim_empresa = spark.read.parquet(os.path.join(GOLD_DIR, "dim_empresa")).alias("dim_empresa")
    dim_tempo = spark.read.parquet(os.path.join(GOLD_DIR, "dim_tempo")).alias("dim_tempo")
    dim_voo = spark.read.parquet(os.path.join(GOLD_DIR, "dim_tipo_voo")).alias("dim_tipo_voo")
    dim_aeroporto = spark.read.parquet(os.path.join(GOLD_DIR, "dim_aeroporto")).alias("dim_aeroporto")

    df_fato = df \
        .join(dim_empresa, on=["EMPRESA_SIGLA", "EMPRESA_NOME", "EMPRESA_NACIONALIDADE"], how="left") \
        .join(dim_tempo, on="DATA", how="left") \
        .join(dim_voo, on=["NATUREZA", "GRUPO_DE_VOO"], how="left") \
        .join(dim_aeroporto.alias("origem"), df["AEROPORTO_DE_ORIGEM_SIGLA"] == col("origem.AEROPORTO_ICAO"), how="left") \
        .join(dim_aeroporto.alias("destino"), df["AEROPORTO_DE_DESTINO_SIGLA"] == col("destino.AEROPORTO_ICAO"), how="left")

    fato_voo = df_fato.select(
        monotonically_increasing_id().alias("ID_FATO_VOO"),
        col("dim_empresa.ID_EMPRESA"),
        col("dim_tempo.ID_TEMPO"),
        col("dim_tipo_voo.ID_TIPO_VOO"),
        col("origem.ID_AEROPORTO").alias("ID_AEROPORTO_ORIGEM"),
        col("destino.ID_AEROPORTO").alias("ID_AEROPORTO_DESTINO"),
        "PASSAGEIROS_PAGOS", "PASSAGEIROS_GRATIS",
        "CARGA_PAGA_KG", "CARGA_GRATIS_KG", "CORREIO_KG",
        "ASK", "RPK", "ATK", "RTK",
        "COMBUSTIVEL_LITROS", "DISTANCIA_VOADA_KM",
        "DECOLAGENS", "ASSENTOS", "PAYLOAD",
        "HORAS_VOADAS", "BAGAGEM_KG"
    )

    fato_voo.write.mode("overwrite").parquet(os.path.join(GOLD_DIR, "fato_voo"))

    print("✅ Camada gold criada com sucesso.")
