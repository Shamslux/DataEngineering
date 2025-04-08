import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from tasks.download_csv import baixar_csv_anac
from config.params import URL_INDEX_ANAC, CSV_ANAC

with DAG(
    dag_id="anac_pipeline_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",
    catchup=False,
    tags=["anac", "dados", "airflow"],
    description="Pipeline de dados da ANAC com Airflow",
) as dag:

    task_baixar_csv = PythonOperator(
        task_id="baixar_csv_anac",
        python_callable=baixar_csv_anac,
        op_args=[URL_INDEX_ANAC, CSV_ANAC],
    )

    task_baixar_csv
