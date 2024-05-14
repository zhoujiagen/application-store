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
| [Fortio](./fortio/README.md)               | `load`          |
| [sysbench](./benchmark/sysbench/README.md) | `sysbench-tpcc` |

## Data Engineering Applications

| Application                                             | Examples                              |
| :------------------------------------------------------ | :------------------------------------ |
| [Apache ActiveMQ Artemis](./activemq/README.md)         | `stomp.py`                            |
| [Apache Airflow](./airflow/README.md)                   | TODO                                  |
| [Apache Cassandra](./cassandra/README.md)               | CQL                                   |
| [Apache Flink](./flink/README.md)                       | Python                                |
| [Apache Hadoop](./hadoop/README.md)                     | pydoop                                |
| [Apache Kafka](./kafka/README.md)                       | Python, Scala                         |
| [Apache Samza](./samza/README.md)                       | Java(as library)                      |
| [Apache Spark](./spark/README.md)                       | `pyspark`, `spark-shell`, `spark-sql` |
| [Apache TinkerPop](./tinkerpop/README.md)               | HTTP, `gremlin-console`, Alchemy.js   |
| [ClickHouse](./clickhouse/README.md)                    | `clickhouse-client`, Bytebase, Python |
| [ELK](./elk/README.md): Elasticsearch, FileBeat, Kibana | Java app Container                    |
| [etcd](./etcd/README.md)                                | `etcdctl`, Python.                    |
| [Hazelcast](./hazelcast/README.md)                      | MySQL CDC in Java                     |
| [Jupyter Notebook](./jupyter/README.md)                 | `ipython-sql`                         |
| [MinIO](./minio/README.md)                              | Python                                |
| [MongoDB](./mongodb/README.md)                          | NonCluster, Cluter, stats, `wt`       |
| [MySQL](./mysql/README.md)                              | 5.7, 8, Replication                   |
| [PostgreSQL](./postgresql/README.md)                    | pgAdmin                               |
| [RabbitMQ](./rabbitmq/README.md)                        | Python                                |
| [Redis](./redis/README.md)                              | TODO                                  |
| [SQLite](./sqlite/README.md)                            | sqlite-web                            |
| [Vector](./vector/README.md)                            | Nginx log to ClickHouse               |

## Ops

| Application                                 | Examples                        |
| :------------------------------------------ | :------------------------------ |
| [Apache Skywalking](./skywalking/README.md) | Java app                        |
| [Archery](./archery/README.md)              | Fix bugs                        |
| [CoreDNS](./coredns/README.md)              | `etcd` plugin, `dig`            |
| [Envoy](./envoy/README.md)                  | MongoDB, httpbin, JWT Auth      |
| [Harbor](./harbor/README.md)                | None                            |
| [Istio](./istio/README.md)                  | bookinfo                        |
| [Jaeger](./jaeger/README.md)                | Python                          |
| [OpenResty](./openresty/README.md)          | `lua-resty-mysql`               |
| [Portainer](./portainer/README.md)          | -                               |
| [Prometheus](./prometheus/README.md)        | Exporter, AlertMaanger, Grafana |

## Security

| Application                               | Examples                         |
| :---------------------------------------- | :------------------------------- |
| [Keycloak](./keycloak/README.md)          | Admin CLI                        |
| [OPA: Open Policy Agent](./opa/README.md) | `opa`, Python                    |
| [OpenLDAP](./openldap/README.md)          | Apache Directory Studio™, Python |

## Testing

| Application                                  | Examples   |
| :------------------------------------------- | :--------- |
| [Flask](./flask/README.md)                   | JSON       |
| [MailHog](./mailhog/README.md)               | `sendmail` |
| [Testcontainers](./testcontainers/README.md) | Python     |
