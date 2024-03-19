from datetime import datetime, timedelta
from airflow.operators.dummy import DummyOperator
from airflow.models.dag import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator


with DAG(
    dag_id='fullstack_papermill_operator',
    default_args={
        'retries': 0
    },
    schedule='0 0 * * *',
    start_date=datetime(2022, 10, 1),
    catchup=False
) as dag_1:

    start_task = DummyOperator(task_id='start_task', dag=dag_1)

    notebook_task = PapermillOperator(
        task_id="fullstack_ETL_notebook",
        input_nb="/home/admin2/projectfullstack/ETL_process.ipynb",
        output_nb="/home/admin2/projectfullstack/ETL_process-{{ ds }}.ipynb",
        parameters={"execution_date": "{{ ds }}"},
    )

    end_task = DummyOperator(task_id='end_task', dag=dag_1)
    
    start_task >> notebook_task >> end_task
    