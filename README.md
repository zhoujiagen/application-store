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

## Benchmark

| Application                                | Examples        |
| :----------------------------------------- | :-------------- |
| [Fortio](./benchmark/fortio/README.md)     | `load`          |
| [sysbench](./benchmark/sysbench/README.md) | `sysbench-tpcc` |

## Data Engineering

| Application                                                              | Examples                              |
| :----------------------------------------------------------------------- | :------------------------------------ |
| [Apache ActiveMQ Artemis](./data-engineering/activemq/README.md)         | `stomp.py`                            |
| [Apache Airflow](./data-engineering/airflow/README.md)                   | TODO                                  |
| [Apache Cassandra](./data-engineering/cassandra/README.md)               | CQL                                   |
| [Apache Flink](./data-engineering/flink/README.md)                       | Python                                |
| [Apache Hadoop](./data-engineering/hadoop/README.md)                     | pydoop                                |
| [Apache Kafka](./data-engineering/kafka/README.md)                       | Python, Scala                         |
| [Apache Samza](./data-engineering/samza/README.md)                       | Java(as library)                      |
| [Apache Spark](./data-engineering/spark/README.md)                       | `pyspark`, `spark-shell`, `spark-sql` |
| [Apache TinkerPop](./data-engineering/tinkerpop/README.md)               | HTTP, `gremlin-console`, Alchemy.js   |
| [ClickHouse](./data-engineering/clickhouse/README.md)                    | `clickhouse-client`, Bytebase, Python |
| [ELK](./data-engineering/elk/README.md): Elasticsearch, FileBeat, Kibana | Java app Container                    |
| [etcd](./data-engineering/etcd/README.md)                                | `etcdctl`, Python.                    |
| [Hazelcast](./data-engineering/hazelcast/README.md)                      | MySQL CDC in Java                     |
| [Jupyter Notebook](./data-engineering/jupyter/README.md)                 | `ipython-sql`                         |
| [MinIO](./data-engineering/minio/README.md)                              | Python                                |
| [MongoDB](./data-engineering/mongodb/README.md)                          | NonCluster, Cluter, stats, `wt`       |
| [MySQL](./data-engineering/mysql/README.md)                              | 5.7, 8, Replication                   |
| [Neo4j](./data-engineering/neo4j/README.md)                              | JavaScript                            |
| [PostgreSQL](./data-engineering/postgresql/README.md)                    | pgAdmin                               |
| [RabbitMQ](./data-engineering/rabbitmq/README.md)                        | Python                                |
| [Redis](./data-engineering/redis/README.md)                              | TODO                                  |
| [SQLite](./data-engineering/sqlite/README.md)                            | sqlite-web                            |
| [Vector](./data-engineering/vector/README.md)                            | Nginx log to ClickHouse               |

## Ops

| Application                                     | Examples                        |
| :---------------------------------------------- | :------------------------------ |
| [Apache Skywalking](./ops/skywalking/README.md) | Java app                        |
| [Archery](./ops/archery/README.md)              | Fix bugs                        |
| [CoreDNS](./ops/coredns/README.md)              | `etcd` plugin, `dig`            |
| [Envoy](./ops/envoy/README.md)                  | MongoDB, httpbin, JWT Auth      |
| [Harbor](./ops/harbor/README.md)                | None                            |
| [Istio](./ops/istio/README.md)                  | bookinfo                        |
| [Jaeger](./ops/jaeger/README.md)                | Python                          |
| [OpenResty](./ops/openresty/README.md)          | `lua-resty-mysql`               |
| [Portainer](./ops/portainer/README.md)          | -                               |
| [Prometheus](./ops/prometheus/README.md)        | Exporter, AlertMaanger, Grafana |
| [Traefik](./ops/traefik/README.md)              | Docker provider                 |

## Security

| Application                                        | Examples                         |
| :------------------------------------------------- | :------------------------------- |
| [Keycloak](./security/keycloak/README.md)          | Admin CLI                        |
| [OPA: Open Policy Agent](./security/opa/README.md) | `opa`, Python                    |
| [OpenLDAP](./security/openldap/README.md)          | Apache Directory Studio™, Python |

## Testing

| Application                                          | Examples   |
| :--------------------------------------------------- | :--------- |
| [Flask](./testing/flask/README.md)                   | JSON       |
| [MailHog](./testing/mailhog/README.md)               | `sendmail` |
| [Testcontainers](./testing/testcontainers/README.md) | Python     |
