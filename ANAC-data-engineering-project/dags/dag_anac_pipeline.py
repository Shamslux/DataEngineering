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
