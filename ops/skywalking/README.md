# SkyWalking

## Java Agent

- supported list: https://skywalking.apache.org/docs/skywalking-java/v9.0.0/en/setup/service-agent/java-agent/supported-list/
- `config/agent.config`: https://skywalking.apache.org/docs/skywalking-java/v9.0.0/en/setup/service-agent/java-agent/configurations/

目录说明:

```shell
# tree
.
├── activations # 激活的组件
│   ├── apm-jdk-forkjoinpool-plugin-9.0.0.jar
│   ├── apm-jdk-http-plugin-9.0.0.jar
│   ├── apm-jdk-threading-plugin-9.0.0.jar
│   ├── apm-jdk-threadpool-plugin-9.0.0.jar
│   ├── apm-toolkit-kafka-activation-9.0.0.jar
│   ├── apm-toolkit-log4j-1.x-activation-9.0.0.jar
│   ├── apm-toolkit-log4j-2.x-activation-9.0.0.jar
│   ├── apm-toolkit-logback-1.x-activation-9.0.0.jar
│   ├── apm-toolkit-logging-common-9.0.0.jar
│   ├── apm-toolkit-meter-activation-9.0.0.jar
│   ├── apm-toolkit-micrometer-activation-9.0.0.jar
│   ├── apm-toolkit-opentracing-activation-9.0.0.jar
│   ├── apm-toolkit-trace-activation-9.0.0.jar
│   └── apm-toolkit-webflux-activation-9.0.0.jar
├── bootstrap-plugins
├── config
│   └── agent.config
├── LICENSE
├── licenses
│   └── LICENSE-asm.txt
├── logs
│   └── skywalking-api.log
├── NOTICE
├── optional-plugins # 可选插件
│   ├── apm-customize-enhance-plugin-9.0.0.jar
│   ├── apm-ehcache-2.x-plugin-9.0.0.jar
│   ├── apm-fastjson-1.x-plugin-9.0.0.jar
│   ├── apm-gson-2.x-plugin-9.0.0.jar
│   ├── apm-guava-cache-plugin-9.0.0.jar
│   ├── apm-jackson-2.x-plugin-9.0.0.jar
│   ├── apm-kotlin-coroutine-plugin-9.0.0.jar
│   ├── apm-mybatis-3.x-plugin-9.0.0.jar
│   ├── apm-nacos-client-2.x-plugin-9.0.0.jar
│   ├── apm-quartz-scheduler-2.x-plugin-9.0.0.jar
│   ├── apm-resttemplate-6.x-plugin-9.0.0.jar
│   ├── apm-sentinel-1.x-plugin-9.0.0.jar
│   ├── apm-shenyu-2.4.x-plugin-9.0.0.jar
│   ├── apm-spring-annotation-plugin-9.0.0.jar
│   ├── apm-spring-cloud-gateway-2.0.x-plugin-9.0.0.jar
│   ├── apm-spring-cloud-gateway-2.1.x-plugin-9.0.0.jar
│   ├── apm-spring-cloud-gateway-3.x-plugin-9.0.0.jar
│   ├── apm-springmvc-annotation-6.x-plugin-9.0.0.jar
│   ├── apm-spring-tx-plugin-9.0.0.jar
│   ├── apm-spring-webflux-5.x-plugin-9.0.0.jar
│   ├── apm-trace-ignore-plugin-9.0.0.jar
│   ├── apm-zookeeper-3.4.x-plugin-9.0.0.jar
│   └── trace-sampler-cpu-policy-plugin-9.0.0.jar
├── optional-reporter-plugins
│   ├── kafka-reporter-plugin-9.0.0.jar
│   ├── lz4-java-1.6.0.jar
│   ├── snappy-java-1.1.7.3.jar
│   └── zstd-jni-1.4.3-1.jar
├── plugins # 实际使用的插件: 可以移除未使用的插件
│   ├── apm-activemq-5.x-plugin-9.0.0.jar
│   ├── apm-aerospike-plugin-9.0.0.jar
│   ├── apm-armeria-0.84.x-plugin-9.0.0.jar
│   ├── apm-armeria-0.85.x-plugin-9.0.0.jar
│   ├── apm-armeria-1.0.x-plugin-9.0.0.jar
│   ├── apm-asynchttpclient-2.x-plugin-9.0.0.jar
│   ├── apm-avro-plugin-9.0.0.jar
│   ├── apm-canal-1.x-plugin-9.0.0.jar
│   ├── apm-cassandra-java-driver-3.x-plugin-9.0.0.jar
│   ├── apm-clickhouse-0.3.1-plugin-9.0.0.jar
│   ├── apm-clickhouse-0.3.2.x-plugin-9.0.0.jar
│   ├── apm-cxf-3.x-plugin-9.0.0.jar
│   ├── apm-dubbo-2.7.x-plugin-9.0.0.jar
│   ├── apm-dubbo-3.x-plugin-9.0.0.jar
│   ├── apm-dubbo-plugin-9.0.0.jar
│   ├── apm-elastic-job-2.x-plugin-9.0.0.jar
│   ├── apm-elasticjob-3.x-plugin-9.0.0.jar
│   ├── apm-elasticsearch-5.x-plugin-9.0.0.jar
│   ├── apm-elasticsearch-6.x-plugin-9.0.0.jar
│   ├── apm-elasticsearch-7.x-plugin-9.0.0.jar
│   ├── apm-feign-default-http-9.x-plugin-9.0.0.jar
│   ├── apm-finagle-6.25.x-plugin-9.0.0.jar
│   ├── apm-grizzly-2.x-4.x-work-threadpool-plugin-9.0.0.jar
│   ├── apm-grizzly-2.x-plugin-9.0.0.jar
│   ├── apm-grpc-1.x-plugin-9.0.0.jar
│   ├── apm-guava-eventbus-plugin-9.0.0.jar
│   ├── apm-h2-1.x-plugin-9.0.0.jar
│   ├── apm-hbase-1.x-2.x-plugin-9.0.0.jar
│   ├── apm-hikaricp-3.x-4.x-plugin-9.0.0.jar
│   ├── apm-httpasyncclient-4.x-plugin-9.0.0.jar
│   ├── apm-httpclient-3.x-plugin-9.0.0.jar
│   ├── apm-httpClient-4.x-plugin-9.0.0.jar
│   ├── apm-httpclient-5.x-plugin-9.0.0.jar
│   ├── apm-httpclient-commons-9.0.0.jar
│   ├── apm-hutool-http-5.x-plugin-9.0.0.jar
│   ├── apm-hystrix-1.x-plugin-9.0.0.jar
│   ├── apm-impala-jdbc-2.6.x-plugin-9.0.0.jar
│   ├── apm-influxdb-2.x-plugin-9.0.0.jar
│   ├── apm-jdbc-commons-9.0.0.jar
│   ├── apm-jersey-2.x-plugin-9.0.0.jar
│   ├── apm-jersey-3.x-plugin-9.0.0.jar
│   ├── apm-jetty-client-11.x-plugin-9.0.0.jar
│   ├── apm-jetty-client-9.0-plugin-9.0.0.jar
│   ├── apm-jetty-client-9.x-plugin-9.0.0.jar
│   ├── apm-jetty-server-11.x-plugin-9.0.0.jar
│   ├── apm-jetty-server-9.x-plugin-9.0.0.jar
│   ├── apm-jetty-thread-pool-plugin-9.0.0.jar
│   ├── apm-kafka-commons-9.0.0.jar
│   ├── apm-kafka-plugin-9.0.0.jar
│   ├── apm-kylin-jdbc-2.6.x-3.x-4.x-plugin-9.0.0.jar
│   ├── apm-lettuce-5.x-plugin-9.0.0.jar
│   ├── apm-light4j-plugin-9.0.0.jar
│   ├── apm-mariadb-2.x-plugin-9.0.0.jar
│   ├── apm-mongodb-2.x-plugin-9.0.0.jar
│   ├── apm-mongodb-3.x-plugin-9.0.0.jar
│   ├── apm-mongodb-4.x-plugin-9.0.0.jar
│   ├── apm-mssql-commons-9.0.0.jar
│   ├── apm-mssql-jdbc-plugin-9.0.0.jar
│   ├── apm-mssql-jtds-1.x-plugin-9.0.0.jar
│   ├── apm-mysql-5.x-plugin-9.0.0.jar
│   ├── apm-mysql-6.x-plugin-9.0.0.jar
│   ├── apm-mysql-8.x-plugin-9.0.0.jar
│   ├── apm-mysql-commons-9.0.0.jar
│   ├── apm-neo4j-4.x-plugin-9.0.0.jar
│   ├── apm-netty-socketio-plugin-9.0.0.jar
│   ├── apm-nutz-http-1.x-plugin-9.0.0.jar
│   ├── apm-nutz-mvc-annotation-1.x-plugin-9.0.0.jar
│   ├── apm-okhttp-3.x-plugin-9.0.0.jar
│   ├── apm-okhttp-4.x-plugin-9.0.0.jar
│   ├── apm-okhttp-common-9.0.0.jar
│   ├── apm-play-2.x-plugin-9.0.0.jar
│   ├── apm-postgresql-8.x-plugin-9.0.0.jar
│   ├── apm-pulsar-2.2-2.7-plugin-9.0.0.jar
│   ├── apm-pulsar-2.8.x-plugin-9.0.0.jar
│   ├── apm-pulsar-common-9.0.0.jar
│   ├── apm-quasar-plugin-9.0.0.jar
│   ├── apm-rabbitmq-plugin-9.0.0.jar
│   ├── apm-redisson-3.x-plugin-9.0.0.jar
│   ├── apm-resttemplate-3.x-plugin-9.0.0.jar
│   ├── apm-resttemplate-4.3.x-plugin-9.0.0.jar
│   ├── apm-rocketmq-3.x-plugin-9.0.0.jar
│   ├── apm-rocketmq-4.x-plugin-9.0.0.jar
│   ├── apm-rocketMQ-5.x-plugin-9.0.0.jar
│   ├── apm-rocketmq-client-java-5.x-plugin-9.0.0.jar
│   ├── apm-servicecomb-java-chassis-2.x-plugin-9.0.0.jar
│   ├── apm-sharding-sphere-3.x-plugin-9.0.0.jar
│   ├── apm-shardingsphere-4.0.x-plugin-9.0.0.jar
│   ├── apm-sharding-sphere-4.1.0-plugin-9.0.0.jar
│   ├── apm-shardingsphere-5.0.0-plugin-9.0.0.jar
│   ├── apm-solrj-7.x-plugin-9.0.0.jar
│   ├── apm-spring-async-annotation-plugin-9.0.0.jar
│   ├── apm-spring-cloud-feign-1.x-plugin-9.0.0.jar
│   ├── apm-spring-cloud-feign-2.x-plugin-9.0.0.jar
│   ├── apm-spring-concurrent-util-4.x-plugin-9.0.0.jar
│   ├── apm-spring-core-patch-9.0.0.jar
│   ├── apm-spring-kafka-1.x-plugin-9.0.0.jar
│   ├── apm-spring-kafka-2.x-plugin-9.0.0.jar
│   ├── apm-springmvc-annotation-3.x-plugin-9.0.0.jar
│   ├── apm-springmvc-annotation-4.x-plugin-9.0.0.jar
│   ├── apm-springmvc-annotation-5.x-plugin-9.0.0.jar
│   ├── apm-springmvc-annotation-commons-9.0.0.jar
│   ├── apm-spring-scheduled-annotation-plugin-9.0.0.jar
│   ├── apm-spymemcached-2.x-plugin-9.0.0.jar
│   ├── apm-struts2-2.x-plugin-9.0.0.jar
│   ├── apm-tomcat-thread-pool-plugin-9.0.0.jar
│   ├── apm-undertow-2.x-plugin-9.0.0.jar
│   ├── apm-undertow-worker-thread-pool-plugin-9.0.0.jar
│   ├── apm-vertx-core-3.x-plugin-9.0.0.jar
│   ├── apm-vertx-core-4.x-plugin-9.0.0.jar
│   ├── apm-xmemcached-2.x-plugin-9.0.0.jar
│   ├── apm-xxl-job-2.x-plugin-9.0.0.jar
│   ├── baidu-brpc-3.x-plugin-9.0.0.jar
│   ├── baidu-brpc-plugin-9.0.0.jar
│   ├── dbcp-2.x-plugin-9.0.0.jar
│   ├── druid-1.x-plugin-9.0.0.jar
│   ├── dubbo-2.7.x-conflict-patch-9.0.0.jar
│   ├── dubbo-3.x-conflict-patch-9.0.0.jar
│   ├── dubbo-conflict-patch-9.0.0.jar
│   ├── graphql-12.x-15.x-plugin-9.0.0.jar
│   ├── graphql-16plus-plugin-9.0.0.jar
│   ├── graphql-8.x-plugin-9.0.0.jar
│   ├── graphql-9.x-plugin-9.0.0.jar
│   ├── jedis-2.x-3.x-plugin-9.0.0.jar
│   ├── jedis-4.x-plugin-9.0.0.jar
│   ├── jsonrpc4j-1.x-plugin-9.0.0.jar
│   ├── micronaut-http-client-plugin-9.0.0.jar
│   ├── micronaut-http-server-plugin-9.0.0.jar
│   ├── motan-plugin-9.0.0.jar
│   ├── nats-2.14.x-2.15.x-plugin-9.0.0.jar
│   ├── okhttp-2.x-plugin-9.0.0.jar
│   ├── resteasy-server-3.x-plugin-9.0.0.jar
│   ├── resteasy-server-4.x-plugin-9.0.0.jar
│   ├── resteasy-server-6.x-plugin-9.0.0.jar
│   ├── resttemplate-commons-9.0.0.jar
│   ├── sofa-rpc-plugin-9.0.0.jar
│   ├── spring-commons-9.0.0.jar
│   ├── spring-webflux-5.x-webclient-plugin-9.0.0.jar
│   ├── thrift-plugin-9.0.0.jar
│   ├── tomcat-10x-plugin-9.0.0.jar
│   ├── tomcat-7.x-8.x-plugin-9.0.0.jar
│   └── websphere-liberty-23.x-plugin-9.0.0.jar
└── skywalking-agent.jar # The agent

8 directories, 188 files
```

例: Java应用 `java-app1`

```dockerfile
...
ENV JAVA_AGENT="-javaagent:/home/app/skywalking-agent/skywalking-agent.jar"
...
ENTRYPOINT ["sh","-c","java ${JAVA_AGENT} -jar app.jar ${JAVA_OPTS} -Dfile.encoding=UTF-8 -Dspring.profiles.active=dev"]
```

```yaml
version: '3.8'

services:
  java-app1:
    image: dev/java-app1
    container_name: java-app1
    labels:
      app.language: Java
      app.type: Backend
    volumes:
      - "/opt/apm/skywalking-agent:/home/app/skywalking-agent"
    environment:
      - "SW_AGENT_NAME=java-app1"
      - "SW_AGENT_COLLECTOR_BACKEND_SERVICES=skywalking-oap-server:11800"
    networks:
      - apm-network

networks:
  apm-network:
    external: true
```