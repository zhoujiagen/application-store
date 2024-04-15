# Testcontainers
- https://testcontainers.com/

## Python
- https://testcontainers-python.readthedocs.io/en/latest/

```shell
# Windows WSL
$ python --version
Python 3.11.5
$ python -m virtualenv .venv
$ source .venv/Scripts/activate
$ pip install testcontainers
$ pip install SQLAlchemy
$ pip freeze > requirements.txt
```

### MySQL
- https://testcontainers-python.readthedocs.io/en/latest/modules/mysql/README.html

```shell
$ pip install pymysql
$ pip install cryptography
$ pip freeze > requirements.txt

$ python ex_mysql.py
...
8.0.36
```

### PostgreSQL

```shell
$ pip install psycopg2
$ pip freeze > requirements.txt

$ python ex_postgresql.py
...
PostgreSQL 16.2 (Debian 16.2-1.pgdg120+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
```

### Kafka

```shell
$ pip install kafka-python
$ pip freeze > requirements.txt

$ python ex_kafka.py 
...
localhost:49723
RecordMetadata(topic='quickstart-events-python', partition=0, topic_partition=TopicPartition(topic='quickstart-events-python', partition=0), offset=0, timestamp=1712905110114, log_start_offset=0, checksum=None, serialized_key_size=-1, serialized_value_size=38, serialized_header_size=-1)
ConsumerRecord(topic='quickstart-events-python', partition=0, offset=0, timestamp=1712905110114, timestamp_type=0, key=None, value=b'hello, i am producer from kafka-python', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=38, serialized_header_size=-1)
```