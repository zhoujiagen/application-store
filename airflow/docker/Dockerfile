# FROM apache/airflow:2.7.3
FROM apache/airflow:2.8.0-python3.11
COPY requirements.txt .

USER airflow
RUN pip install -r requirements.txt --no-cache-dir

# PlayWright
# https://stackoverflow.com/questions/72431221/whats-the-best-way-to-setup-playwright-in-apache-airflow-in-docker
USER root
RUN apt-get update
RUN python3 -m pip install playwright 
RUN python3 -m playwright install --with-deps chromium