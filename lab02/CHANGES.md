# Изменения между lab01 и lab02



## Что добавлено во 2-й лабораторной работе

### 1. Spark кластер

**Добавлены новые сервисы в docker-compose.yml:**

| Сервис | Роль | Порт |
|--------|------|------|
| `spark-master` | Координатор распределённых вычислений | 4040 (UI), 7077 (connection) |
| `spark-worker` | Исполнитель задач | 7000 |

**Почему это нужно:** В 1-й работе все задачи выполнялись на одном контейнере. Spark позволяет распределить вычисления на множество воркеров.

### 2. Новый оператор — SparkSubmitOperator

**Было (лаба 1):**
```python
# Простые операторы
task = BashOperator(
    task_id='hello',
    bash_command='echo "Hello World"',
    dag=dag,
)
```

**Стало (лаба 2):**
# Spark оператор для распределённых вычислений
```python
run_spark_job = SparkSubmitOperator(
    task_id='run_spark_job',
    application='/opt/airflow/spark/main.py',
    conn_id='spark_default',
    verbose=True,
    dag=dag,
)
```
### 3. Новые зависимости в Dockerfile
```
+ USER root
+ RUN apt update && apt install -y procps default-jre && apt clean
+ USER airflow
+ RUN pip install apache-airflow-providers-apache-spark==4.1.1 pyspark==3.5.0
```

### 4. docker-compose
```
volumes:
  - ./dags:/opt/airflow/dags
  - ./logs:/opt/airflow/logs
  - ./config:/opt/airflow/config
  - ./plugins:/opt/airflow/plugins
+ - ./spark:/opt/airflow/spark
```

### 5. Изменения в порядке запуска сервисов

**lab01**
postgres → airflow-init → airflow-webserver → airflow-scheduler

**lab02**
postgres → spark-master → spark-worker → airflow-init → airflow-webserver → airflow-scheduler