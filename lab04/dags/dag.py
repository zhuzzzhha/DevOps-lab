from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
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
    description='Run a small Spark job and expose useful logs for observability',
    schedule_interval='@daily',
    catchup=False,
    tags=['spark', 'observability', 'lab4'],
)

start = EmptyOperator(
    task_id='start_pipeline',
    dag=dag,
)

run_spark_job = SparkSubmitOperator(
    task_id='run_spark_job',
    application='/opt/airflow/spark/main.py',
    name='spark-job',
    conn_id='spark_default',
    application_args=['--run-id', '{{ run_id }}'],
    verbose=True,
    dag=dag,
)

finish = EmptyOperator(
    task_id='finish_pipeline',
    dag=dag,
)

start >> run_spark_job >> finish
