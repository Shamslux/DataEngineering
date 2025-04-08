import os

BASE_DATA_DIR = "/opt/airflow/data"


BRONZE_DIR = os.path.join(BASE_DATA_DIR, "bronze")
SILVER_DIR = os.path.join(BASE_DATA_DIR, "silver")
GOLD_DIR   = os.path.join(BASE_DATA_DIR, "gold")
CSV_ANAC = os.path.join(BRONZE_DIR, "Dados_Estatisticos.csv")
PARQUET_ANAC_2023 = os.path.join(SILVER_DIR, "anac_data.parquet")

URL_INDEX_ANAC = "https://sistemas.anac.gov.br/dadosabertos/Voos%20e%20operações%20aéreas/Dados%20Estatísticos%20do%20Transporte%20Aéreo/"


