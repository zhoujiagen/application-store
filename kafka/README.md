# Kafka

- https://github.com/apache/kafka/tree/trunk/docker
- https://hub.docker.com/r/apache/kafka
- alternative: [bitnami/kafka](https://hub.docker.com/r/bitnami/kafka)

```shell
$ vi /etc/kafka/docker/launch
...
exec /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties
```

```shell
# Terminal 1
$ docker exec -it kafka-broker bash 
1740adfd05ab:/$ cd /opt/kafka/
1740adfd05ab:/opt/kafka$ bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
Created topic quickstart-events.
1740adfd05ab:/opt/kafka$ bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
Topic: quickstart-events        TopicId: _Y_ebTzURTuk0wTOL_QBdQ PartitionCount: 1       ReplicationFactor: 1    Configs: segment.bytes=1073741824
        Topic: quickstart-events        Partition: 0    Leader: 1       Replicas: 1     Isr: 1
1740adfd05ab:/opt/kafka$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
>This is my first event
>This is my second event

# Terminal 2
$ docker exec -it kafka-broker bash
1740adfd05ab:/$ cd /opt/kafka/
1740adfd05ab:/opt/kafka$ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
This is my first event

This is my first event
This is my second event
```

## kafka-ui

- https://github.com/provectus/kafka-ui
- [cookdoc: Setting up a Local Kafka Environment in KRaft Mode with Docker-Compose and Bitnami Image, Enhanced by Provectus Kafka-UI](https://medium.com/@tetianaokhotnik/setting-up-a-local-kafka-environment-in-kraft-mode-with-docker-compose-and-bitnami-image-enhanced-29a2dcabf2a9)

```properties
# server.properties
# DEPLOY_ENV
advertised.listeners=PLAINTEXT://kafka-broker:9092
```

Access `http://localhost:18080/`

Kafka Cluser
- Cluster name: `kafka-broker`
- Bootstrap servers: `kafka-broker`, `9092`

## Clients

### Out Container Access

- [cookdoc](https://medium.com/@tetianaokhotnik/setting-up-a-local-kafka-environment-in-kraft-mode-with-docker-compose-and-bitnami-image-enhanced-29a2dcabf2a9): use `bitnami/kafka:3.4`.

Add `EXTERNAL`

```properties
# server.properties
listeners=PLAINTEXT://:9092,CONTROLLER://:9093,EXTERNAL://:9094
advertised.listeners=PLAINTEXT://127.0.0.1:9092,EXTERNAL://192.168.3.182:9094
```

### Python

- https://kafka-python.readthedocs.io/en/master/

```shell
# Windows WSL
$ python --version
Python 3.11.5
$ python -m virtualenv .venv
$ source .venv/Scripts/activate
$ pip install kafka-python
$ pip freeze > requirements.txt

# make user topic 'quickstart-events' exist

$ python producer.py
$ python consumer.py
```

### Java/Scala

- https://github.com/com-lihaoyi/Ammonite 

```shell
# Terminal 1
$ amm --watch producer.sc

# Terminal 2
$ amm --watch consumer.sc 
```
