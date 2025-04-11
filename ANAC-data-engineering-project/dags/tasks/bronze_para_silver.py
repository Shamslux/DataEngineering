# tasks/bronze_para_silver.py

import os
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnan, when, regexp_replace, trim, to_date, concat_ws, lit, lpad
from pyspark.sql.types import StringType, DoubleType, IntegerType

from config.params import BRONZE_DIR, SILVER_DIR

def bronze_para_silver():
    print("🚀 Iniciando transformação da camada Bronze para Silver...")

    caminho_csv = os.path.join(BRONZE_DIR, "Dados_Estatisticos.csv")

    print("📚 Lendo e corrigindo CSV com Pandas (ajuste da primeira linha)...")
    df_pandas = pd.read_csv(caminho_csv, sep=";", skiprows=1)
    csv_corrigido = caminho_csv.replace(".csv", "_limpo.csv")
    df_pandas.to_csv(csv_corrigido, sep=";", index=False)

    print("✨ Inicializando SparkSession...")
    spark = SparkSession.builder \
        .appName("Limpeza e transformação - ANAC") \
        .getOrCreate()

    print("📂 Lendo CSV corrigido com Spark...")
    df_anac = spark.read.csv(csv_corrigido, sep=";", header=True, inferSchema=True)

    print("🧪 Corrigindo tipos de dados e tratando vírgulas como ponto decimal...")
    df_anac = df_anac.withColumn("PASSAGEIROS_PAGOS", col("PASSAGEIROS_PAGOS").cast("int"))
    df_anac = df_anac.withColumn("PASSAGEIROS_GRATIS", col("PASSAGEIROS_GRATIS").cast("int"))
    df_anac = df_anac.withColumn("DECOLAGENS", col("DECOLAGENS").cast("int"))
    df_anac = df_anac.withColumn("HORAS_VOADAS", regexp_replace("HORAS_VOADAS", ",", ".").cast(DoubleType()))

    print("🔍 Tratando valores nulos e ausentes...")
    substituicoes = {}
    for field in df_anac.schema.fields:
        if field.nullable:
            if isinstance(field.dataType, StringType):
                substituicoes[field.name] = "SEM REGISTRO"
            elif isinstance(field.dataType, DoubleType):
                substituicoes[field.name] = 0.0
            elif isinstance(field.dataType, IntegerType):
                substituicoes[field.name] = 0

    for coluna in substituicoes:
        df_anac = df_anac.withColumn(
            coluna,
            when(isnan(col(coluna)), None).otherwise(col(coluna))
        ).fillna({coluna: substituicoes[coluna]})

    print("✂️ Aplicando `trim()` em colunas textuais para remover espaços...")
    for field in df_anac.schema.fields:
        if isinstance(field.dataType, StringType):
            df_anac = df_anac.withColumn(field.name, trim(col(field.name)))

    print("📅 Criando coluna de data completa (DATA)...")
    df_anac = df_anac.withColumn(
        "DATA",
        to_date(
            concat_ws("-", col("ANO"), lpad(col("MES").cast("string"), 2, "0"), lit("01")),
            "yyyy-MM-dd"
        )
    )

    print("💾 Salvando dados tratados na camada Silver particionada por ANO e MES...")
    df_anac.write.mode("overwrite").partitionBy("ANO", "MES").parquet(
        os.path.join(SILVER_DIR, "operacoes_anac_partitioned")
    )

    spark.stop()
    print("✅ Transformação Bronze → Silver concluída com sucesso.")
