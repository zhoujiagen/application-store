# Airflow

Add providers: see `Dockerfile`.

TODO:

- [ ] Add Jinja template support.
- [ ] Add `execution_date`, cron/frequence-based schedule support.
- [ ] HA solution: MySQL, multiple workers, etc.
- [ ] Add BI report support.

Build image with Python dependencies with `requirements.txt`:

```shell
cd docker
docker build -t dev/airflow:2.7.3 .
```

Prepare directories:

```shell
mkdir -p {dags,logs,config,plugins}
```

Run as `root` user (optional, use case: Playwright):

```shell
# .env
AIRFLOW_UID=0

# Dockerfile
USER root

# docker-compose.yaml
  volumes:
    - ./.aws:/root/.aws
```

Start:

```shell
docker compose up -d
```

Initialize MySQL database and users in case of `airflow-init` failed:

```sql
-- MySQL
-- https://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html#setting-up-a-mysql-database
CREATE DATABASE airflow CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'airflow' IDENTIFIED BY 'airflow';
GRANT ALL PRIVILEGES ON airflow_db.* TO 'airflow';
```