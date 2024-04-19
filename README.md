# application-store
Collections of kickoff setup scripts and demonstration examples for applications.

Conventions:

- Use `DEPLOY_ENV` to mark custom settings.
- Use `192.168.3.182` as host IP.

Environments:

- Windows
  - Docker Destop 4.22.1 (118664)
  - Docker Engine v24.0.5
  - Kubernetes v1.27.2

Applications:

| Application                                             | Examples                               |
| :------------------------------------------------------ | :------------------------------------- |
| [Apache ActiveMQ Artemis](./activemq/README.md)         | `stomp.py`                             |
| [Apache Airflow](./airflow/README.md)                   | TODO                                   |
| [Apache Cassandra](./cassandra/README.md)               | CQL                                    |
| [Apache Flink](./flink/README.md)                       | Python                                 |
| [Apache Hadoop](./hadoop/README.md)                     | pydoop                                 |
| [Apache Kafka](./kafka/README.md)                       | Python, Scala                          |
| [Apache Samza](./samza/README.md)                       | Java(as library)                       |
| [Apache Skywalking](./skywalking/README.md)             | Java app                               |
| [Apache Spark](./spark/README.md)                       | `pyspark`, `spark-shell`, `spark-sql`  |
| [Archery](./archery/README.md)                          | Fix bugs                               |
| [ClickHouse](./clickhouse/README.md)                    | `clickhouse-client`, Bytebase, Python. |
| [ELK](./elk/README.md): Elasticsearch, FileBeat, Kibana | Java app Container                     |
| [Envoy](./envoy/README.md)                              | MongoDB, httpbin, JWT Auth             |
| [Flask](./flask/README.md)                              | JSON                                   |
| [Fortio](./fortio/README.md)                            | `load`                                 |
| [Harbor](./harbor/README.md)                            | None                                   |
| [Hazelcast](./hazelcast/README.md)                      | MySQL CDC in Java                      |
| [Istio](./istio/README.md)                              | bookinfo                               |
| [Jaeger](./jaeger/README.md)                            | Python                                 |
| [Keycloak](./keycloak/README.md)                        | Admin CLI                              |
| [MailHog](./mailhog/README.md)                          | `sendmail`                             |
| [MinIO](./minio/README.md)                              | Python                                 |
| [MongoDB](./mongodb/README.md)                          | NonCluster, Cluter, stats, `wt`        |
| [MySQL](./mysql/README.md)                              | 5.7, 8, Replication                    |
| [OPA: Open Policy Agent](./opa/README.md)               | `opa`, Python                          |
| [OpenResty](./openresty/README.md)                      | `lua-resty-mysql`                      |
| [PostgreSQL](./postgresql/README.md)                    | pgAdmin                                |
| [Prometheus](./prometheus/README.md)                    | Exporter, AlertMaanger, Grafana        |
| [RabbitMQ](./rabbitmq/README.md)                        | Python                                 |
| [Redis](./redis/README.md)                              | TODO                                   |
| [SQLite](./sqlite/README.md)                            | sqlite-web                             |
| [Testcontainers](./testcontainers/README.md)            | Python                                 |
| [Vector](./vector/README.md)                            | Nginx log to ClickHouse                |
