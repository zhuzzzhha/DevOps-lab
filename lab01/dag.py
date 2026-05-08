from datetime import datetime, timedelta
import random
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'me',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2026, 5, 8),
}

def generate_numbers(**kwargs):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    kwargs['ti'].xcom_push(key='a', value=a)
    kwargs['ti'].xcom_push(key='b', value=b)
    print(f"Generated numbers: a={a}, b={b}")
    return a, b

def add_numbers(**kwargs):
    ti = kwargs['ti']
    a = ti.xcom_pull(task_ids='generate', key='a')
    b = ti.xcom_pull(task_ids='generate', key='b')
    result = a + b
    ti.xcom_push(key='sum', value=result)
    print(f"Sum: {result}")
    return result

def multiply_result(**kwargs):
    ti = kwargs['ti']
    s = ti.xcom_pull(task_ids='add', key='sum')
    result = s * 2
    print(f"Final result (sum * 2): {result}")
    return result

with DAG(
    dag_id='simple_math_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['lab1'],
) as dag:

    generate = PythonOperator(
        task_id='generate',
        python_callable=generate_numbers,
    )

    add = PythonOperator(
        task_id='add',
        python_callable=add_numbers,
    )

    multiply = PythonOperator(
        task_id='multiply',
        python_callable=multiply_result,
    )

    generate >> add >> multiply
