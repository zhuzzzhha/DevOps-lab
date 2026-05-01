FROM apache/airflow:2.7.1

WORKDIR /opt/airflow

COPY ./dags /opt/airflow/dags

# (Опционально) Если есть файлы с переменными, подключениями и т.д. — скопируйте их тоже
# COPY ./airflow.cfg /opt/airflow/airflow.cfg
# COPY ./requirements.txt /opt/airflow/requirements.txt

# (Опционально) Установка дополнительных Python-пакетов, если они есть
# RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# Команда запуска по умолчанию (наследуется от базового образа)
# CMD ["airflow", "standalone"] 