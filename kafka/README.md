# Kafka

- https://github.com/apache/kafka/tree/trunk/docker

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