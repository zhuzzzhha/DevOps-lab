from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
    'owner': 'me',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    dag_id='spark_job_dag',
    default_args=default_args,
    description='Запуск Spark задачи из папки spark',
    schedule_interval='@daily',
    catchup=False,
)

run_spark_job = SparkSubmitOperator(
    task_id='run_spark_job',
    application='/opt/airflow/spark/main.py', 
    name='spark-job',
    conn_id='spark_default',
    verbose=True,
    dag=dag,
)

run_spark_job