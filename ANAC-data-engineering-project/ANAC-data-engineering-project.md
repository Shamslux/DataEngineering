![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Spark](https://img.shields.io/badge/Apache_Spark-FFFFFF?style=for-the-badge&logo=apachespark&logoColor=#E35A16)
![PBI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=white)
![GPT](https://img.shields.io/badge/ChatGPT%204o-000000?style=for-the-badge&logo=openai&logoColor=white&label=)

<div align="left">
  <img src="https://github.com/user-attachments/assets/50e1afad-2495-481b-ac3b-a07d3e8fbfda" alt="Badge" width="150">
</div>

<div align="right">
  <img src="https://github.com/user-attachments/assets/a0d71de3-788b-474a-8369-ec40f44901a5" alt="Badge" width="150">
</div>

# Projeto ANAC - Engenharia de Dados

Fala, pessoal, tudo certinho? Aqui é o João (aka `Shamslux`). Gostaria de compartilhar com vocês um pouco sobre esse mais novo projeto
que criei. Nele eu utilizei dados abertos do governo federal, em especial, dados sobre operações aéreas sobre território nacional, ao
longo de 25 anos. 

Antes de prosseguir em mais explicações, contudo, gostaria de inormar que subi um vídeo no YouTube para facilitar a explicação do projeto.
Sei que nem todos vão ter o tempo (ou paciência, rs) para ler a documentação aqui, então podem assistir ao meu vídeo (em 2x, de preferência).

Segue o link abaixo (só clicar nessa imagem que ela vai levá-lo ao YouTube:

[![Apresentação do Projeto ANAC](https://img.youtube.com/vi/NVXTRQ6NOS4/0.jpg)](https://youtu.be/NVXTRQ6NOS4)

# Tecnologias, metodologias e ferramentas

De forma suscinta, utilizei:

- Airflow (orquestrador dos pipelines) + PySpark (para rodar direto no container do Airflow)
- Spark + Jupyter (para testar com notebooks as futuras tasks da DAG)
- Python (base para o Airflow, Jupyter e PySpark)
- Docker (basicamente nossa infraestrutura toda nele)

A ideia foi criar um pequeno Lakehouse, organizado em camadas (bronze, silver e gold) para que o processo de extração dos dados da ANAC seguisse uma lógica
próxima ao que vemos nos pipelines do mundo real, isto é, uma extração do CSV da base da ANAC, tratamentos realizados em código e aplicação da metodologia
de inteligência de negócios (BI) para obtenção das informações e insights possíveis.

# DataOps - A infraestrutura do nosso projeto

O projeto todo usou o recurso do Docker em minha máquina local. Aqui estão os arquivos usados:

## Docker Compose

```yaml
version: "3.8"

#########################
#------ POSTGRES -------#
#########################
services:

  postgres:
    image: postgres:14
    container_name: pg-anac
    restart: always
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

#########################
#-------- AIRFLOW -------#
#########################
  airflow:
    build:
      context: .
      dockerfile: Dockerfile.airflow
    container_name: airflow-anac
    depends_on:
      - postgres
    restart: always
    user: "0:0"  
    ports:
      - "8080:8080"
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW__CORE__FERNET_KEY: ''
      AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION: 'False'
      AIRFLOW__CORE__LOAD_EXAMPLES: 'False'
    volumes:
      - ./dags:/opt/airflow/dags
      - ./logs:/opt/airflow/logs
      - ./plugins:/opt/airflow/plugins
      - ./data:/opt/airflow/data
    command: >
      bash -c "
        airflow db upgrade &&
        airflow users create --username admin --firstname Admin --lastname User --role Admin --password admin --email admin@example.com &&
        airflow scheduler & 
        exec airflow webserver"

#########################
#-------- SPARK --------#
#########################
  spark:
    image: bitnami/spark:latest
    container_name: spark-anac
    ports:
      - "4040:4040"  
    volumes:
      - ./data:/data
    environment:
      - SPARK_MODE=master

#########################
#------- JUPYTER -------#
#########################
  jupyter:
    image: jupyter/pyspark-notebook
    container_name: jupyter-anac
    ports:
      - "8888:8888"
    volumes:
      - ./data:/home/jovyan/data
      - ./notebooks:/home/jovyan/work
    environment:
      - PYSPARK_PYTHON=python3
      - PYSPARK_DRIVER_PYTHON=jupyter
      - PYSPARK_DRIVER_PYTHON_OPTS=notebook
      - SPARK_OPTS=--driver-memory 2g
    depends_on:
      - spark

#########################
#------ VOLUMES --------#
#########################
volumes:
  pgdata:
```
## Docker File Airflow
```yaml
FROM apache/airflow:2.8.1-python3.10

# Modo root temporariamente para instalar o Java
USER root

# Instala o OpenJDK 17 (para compatibilidade com PySpark)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Define variáveis de ambiente do Java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"
ENV PIP_DEFAULT_TIMEOUT=100

# Copia o requirements.txt
COPY requirements.txt /requirements.txt

# Volta ao usuário padrão do Airflow
USER airflow

# Instala primeiro o PySpark separadamente para evitar timeout
RUN pip install --no-cache-dir pyspark==3.5.0 && \
    pip install --no-cache-dir -r /requirements.txt
```
## Requirements
```txt
requests            
pandas              
pyarrow             
openpyxl            
lxml                
beautifulsoup4      
python-dotenv
pyspark       
holidays
```
Eu cheguei sim a ter problemas com o ambiente, mas fui buscando soluções. Em geral, usei a IA generativa (GPT 4o) para me auxiliar e fui conduzindo essa IA para resolver os problemas (ela sozinha não dá conta de resolver, deixando logo a dica, tem que guiá-la e prestar atenção).
O bom desses "erros" durante esses projetos de estudo é justamente porque, na vida real, é muito comum a existência de erros e vamos precisar lidar com eles quase diariamente.

# Airflow

## DAG

Vamos ver agora a estrutura da nossa DAG:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

from tasks.download_csv import baixar_csv_anac
from tasks.bronze_para_silver import bronze_para_silver
from tasks.silver_para_gold import silver_para_gold
from config.params import URL_INDEX_ANAC, CSV_ANAC

# Definição da DAG
with DAG(
    dag_id="anac_pipeline_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",
    catchup=False,
    tags=["anac", "dados", "airflow"],
    description="Pipeline de dados da ANAC com Airflow",
) as dag:

    # Marca visual de início
    begin = DummyOperator(task_id="begin")

    # Tarefa de download da ANAC
    task_baixar_csv = PythonOperator(
        task_id="baixar_csv_anac",
        python_callable=baixar_csv_anac,
        op_args=[URL_INDEX_ANAC, CSV_ANAC],
    )

    # Bronze -> Silver
    task_transformar_para_silver = PythonOperator(
        task_id="bronze_para_silver",
        python_callable=bronze_para_silver,
    )

    # Silver -> Gold
    task_transformar_para_gold = PythonOperator(
        task_id="silver_para_gold",
        python_callable=silver_para_gold
    )


    # Marca visual de fim
    end = DummyOperator(task_id="end")

    # Definição da ordem de execução
    begin >> task_baixar_csv >> task_transformar_para_silver >> task_transformar_para_gold >> end
```

## Tasks

Agora, vejamos as tarefas:

### 1ª tarefa - Baixar o CSV da ANAC

```python
import os
import requests
from bs4 import BeautifulSoup

def baixar_csv_anac(pagina_index_url: str, caminho_salvar: str):
    response = requests.get(pagina_index_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    link_csv = None
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.lower().endswith("dados_estatisticos.csv"):
            link_csv = href
            break

    if not link_csv:
        raise Exception("Arquivo CSV não encontrado na página!")

    if not pagina_index_url.endswith("/"):
        pagina_index_url += "/"
    url_csv = pagina_index_url + link_csv

    print(f"[INFO] Baixando arquivo de: {url_csv}")
    print(f"[DEBUG] Salvando em: {caminho_salvar}")

    os.makedirs(os.path.dirname(caminho_salvar), exist_ok=True)

    csv_response = requests.get(url_csv, stream=True)
    csv_response.raise_for_status()

    with open(caminho_salvar, "wb") as f:
        for chunk in csv_response.iter_content(chunk_size=1048576):  # 1MB
            if chunk:
                f.write(chunk)

    print(f"[SUCESSO] CSV salvo em {caminho_salvar}")
```
### 2ª tarefa - Tratar o conjunto de dados

```python
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
```

### 3ª tarefa - Criando dimensões e fatos

```python
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
```

# Vendo na prática!

Agora, vamos ver como o processo ocorreu na prática!

![airflow-dag-graph-view](https://github.com/user-attachments/assets/41e6b7bc-a12c-4834-a254-a88e3bb0d792)

Aqui temos uma visão gráfica da nossa DAG e suas tasks. A primeira task é executada e temos o donwload do arquivo desejado na camada bronze do nosso Lake.

![task1-log](https://github.com/user-attachments/assets/a5c84a30-2a20-414e-a818-c636688829a7)

![bronze-raw-file-1](https://github.com/user-attachments/assets/13130533-313d-4f7a-a40d-0f2ad63116d9)

---

Depois dessa primeira tarefa, vemos a segunda em execução que cria o arquivo CSV limpo que vimos na imagem anterior (por causa da primeira linha de atualização, o que atrapalhava a leitura e essa versão limpa é apenas um pré-tratamento antes das transformações mais substanciais). 

**Nota: Refletindo agora, penso que talvez volte nesse ponto, apesar de "inocente", caberia uma reflexão se esse arquivo poderia estar na nossa camada bronze ou se outro método poderia ser feito para remediar isso. Mas vou deixar para uma revisitação ao projeto mais pro futuro.**

A segunda tarefa faz ajustes nas colunas `PASSAGEIROS_PAGOS`, `PASSAGEIROS_GRATIS`, `DECOLAGENS` (de `double` para `int`, uma vez que são dados discretos) e `HORAS_VOADAS`(remoção de vírgula para uso de ponto e conversão de `string` para `double`, sendo uma coluna de dados contínuos).
Depois ocorre a remoção de valores nulos, ajustes em registros faltantes e o salvamento particionando por ano e mês.

![airflow-task-2](https://github.com/user-attachments/assets/94640667-3fb4-41db-956a-e9cad9f22e10)

![silver](https://github.com/user-attachments/assets/7bd14f6e-6a80-4567-a76d-ce7550ca3a89)

Finalmente, a terceira tarefa é responsável por criar as dimensões e a fato na camada gold:

![airflow-task-3](https://github.com/user-attachments/assets/f9ecfa21-6bf4-4a64-998a-632752e20563)

![gold](https://github.com/user-attachments/assets/7bb36634-db1c-4376-9868-5577810ca1fd)

---

Terminada a extração, carga e tratamento dos dados, agora que estamos com a última etapa terminada (tratamento/transformação, ELT), vamos verificar como ficou nosso painel final no Power BI:

![pbi](https://github.com/user-attachments/assets/b8121170-b934-4347-9bf7-7f06c6bca91a)

Aqui os relacionamentos em nosso modelo estrela (*star schema*:

![star](https://github.com/user-attachments/assets/e9f4cfe6-c35e-49a2-97e2-085635115517)

Como os dados vieram bem tratados, apenas precisei criar duas medidas, em geral, envolvendo consolidação de alguns dados (ex.: total de passageiro e carga, pois havia mais de uma coluna com valores):

![medidas](https://github.com/user-attachments/assets/c10136af-fdb2-45ed-a513-5afdc1ad2035)

# Últimas Considerações

Bem, agradeço a paciência de ler até aqui. Sei que há pontos de melhorias, sempre precisamos melhorar, mas minha ideia era usar esse projeto para praticar, revisar algumas abordagens e demonstrar um pouco das minhas capacidades com o que já trabalhei no mundo real. Claro
que a vida real é mais complexa e os problemas são mais desafiadores, mas posso ousar dizer que algumas coisas são desafios técnicos, mas 90% dos desafios são problemas e resolução de problemas. 😅




