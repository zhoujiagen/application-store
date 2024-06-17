# Apache Pinot
- https://hub.docker.com/r/apachepinot/pinot

Access Pinot Controller: `http://localhost:9000/`.

```shell
# Copy scripts
docker container cp pinot-controller:/opt/pinot/bin bin

# Copy configuration
docker container cp pinot-controller:/opt/pinot/conf conf
```

## Batch
- https://docs.pinot.apache.org/basics/getting-started/pushing-your-data-to-pinot

```shell
# controller
bin/pinot-admin.sh AddTable \
  -tableConfigFile /tmp/examples/transcript-table-offline.json \
  -schemaFile /tmp/examples/transcript-schema.json -exec
# controller
bin/pinot-admin.sh LaunchDataIngestionJob \
    -jobSpecFile /tmp/examples/batch-job-spec.yml


# Broker Query API
# https://docs.pinot.apache.org/users/api/querying-pinot-using-standard-sql
curl -H "Content-Type: application/json" -X POST \
   -d '{"sql":"SELECT * FROM transcript"}' \
   http://localhost:8099/query/sql
# broker
bin/pinot-admin.sh PostQuery -query="SELECT * FROM transcript"
# controller, server
bin/pinot-admin.sh PostQuery -brokerHost="pinot-broker" -brokerPort=8099 -query="SELECT * FROM transcript"
```

## Stream
- https://docs.pinot.apache.org/basics/getting-started/pushing-your-streaming-data-to-pinot

```shell
# kafka-broker
/opt/bitnami/kafka/bin/kafka-topics.sh \
  --zookeeper pinot-zookeeper:2181/kafka \
  --partitions=1 --replication-factor=1 \
  --create --topic transcript-topic
Created topic "transcript-topic".

# controller
# https://github.com/apache/pinot/blob/master/pinot-plugins/pinot-stream-ingestion/pinot-kafka-base/src/main/java/org/apache/pinot/plugin/stream/kafka/KafkaStreamConfigProperties.java#L28
#       "stream.kafka.broker.list": "192.168.3.198:9094",
#      "stream.kafka.broker.list": "kafka-broker:9092",
bin/pinot-admin.sh AddTable \
  -tableConfigFile /tmp/examples/transcript-table-realtime.json \
  -schemaFile /tmp/examples/transcript-rt-schema.json \
  -exec

# kafka-broker
/opt/bitnami/kafka/bin/kafka-console-producer.sh \
  --broker-list kafka-broker:9092 \
  --topic transcript-topic < /tmp/examples/raw_data/transcript.json
/opt/bitnami/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server kafka-broker:9092 \
  --topic transcript-topic \
  --from-beginning

# controller
bin/pinot-admin.sh PostQuery -brokerHost="pinot-broker" -brokerPort=8099 -query="SELECT * FROM transcriptrt"
```