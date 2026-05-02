from datetime import datetime, timedelta
from airflow import DAG

default_args = {
    'owner': 'me',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    dag_id='my_first_dag',                
    default_args=default_args,
    description='Простой пример DAG',
    schedule_interval='@daily',           
    catchup=False,                        
)