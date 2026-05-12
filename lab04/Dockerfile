FROM apache/airflow:2.7.1

WORKDIR /opt/airflow

# Переключаемся на root для установки системных пакетов
USER root

# Устанавливаем необходимые системные пакеты (procps - для ps, df и т.д.; default-jre - для Java)
RUN apt update && apt install -y procps default-jre && apt clean

# Копируем DAG'и и Spark скрипты (пока от root)
COPY ./dags/* ./dags/
COPY ./spark/* ./spark/

# Возвращаемся к пользователю airflow для установки Python пакетов
USER airflow

# Устанавливаем Python библиотеки для Spark (точно рабочие версии)
RUN pip install --no-cache-dir apache-airflow-providers-apache-spark==4.1.1 pyspark==3.5.0 "airflow-exporter>=1.7,<2"

# Команда запуска по умолчанию (наследуется от базового образа)
# CMD ["airflow", "standalone"]