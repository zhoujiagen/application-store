# Flink

- https://hub.docker.com/_/flink
- https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/resource-providers/standalone/docker/


Dashboard: `http://localhost:8081/`.

History Server Dashboard: `http://localhost:8082/`.

quickstart example:

```shell
# on jobmanager
root@89399ddb24a6:/opt/flink# ls
bin  conf  examples  lib  LICENSE  licenses  log  NOTICE  opt  plugins  README.txt
root@89399ddb24a6:/opt/flink# ./bin/flink run examples/streaming/WordCount.jar
Job has been submitted with JobID 1a8031e6b24ed7449d9b98eae5cb5ab9
Program execution finished
Job with JobID 1a8031e6b24ed7449d9b98eae5cb5ab9 has finished.
Job Runtime: 123 ms
# list all jobs
root@89399ddb24a6:/opt/flink# bin/flink list -a
No running jobs.
No scheduled jobs.
---------------------- Terminated Jobs -----------------------
17.04.2024 01:33:58 : 1a8031e6b24ed7449d9b98eae5cb5ab9 : WordCount (FINISHED)
--------------------------------------------------------------
# view job execution graph
root@89399ddb24a6:/opt/flink# bin/flink info examples/streaming/WordCount.jar
----------------------- Execution Plan -----------------------
{
  "nodes" : [ {
    "id" : 1,
    "type" : "Source: in-memory-input",
    "pact" : "Data Source",
    "contents" : "Source: in-memory-input",
    "parallelism" : 1
  }, {
    "id" : 2,
    "type" : "tokenizer",
    "pact" : "Operator",
    "contents" : "tokenizer",
    "parallelism" : 1,
    "predecessors" : [ {
      "id" : 1,
      "ship_strategy" : "FORWARD",
      "side" : "second"
    } ]
  }, {
    "id" : 4,
    "type" : "counter",
    "pact" : "Operator",
    "contents" : "counter",
    "parallelism" : 1,
    "predecessors" : [ {
      "id" : 2,
      "ship_strategy" : "HASH",
      "side" : "second"
    } ]
  }, {
    "id" : 5,
    "type" : "Sink: print-sink",
    "pact" : "Data Sink",
    "contents" : "Sink: print-sink",
    "parallelism" : 1,
    "predecessors" : [ {
      "id" : 4,
      "ship_strategy" : "FORWARD",
      "side" : "second"
    } ]
  } ]
}
--------------------------------------------------------------

No description provided.

# view configuration
root@89399ddb24a6:/opt/flink# cat conf/config.yaml 
blob:
  server:
    port: '6124'
taskmanager:
  memory:
    process:
      size: 1728m
  bind-host: 0.0.0.0
  numberOfTaskSlots: 1
jobmanager:
  execution:
    failover-strategy: region
  rpc:
    address: jobmanager
    port: 6123
  memory:
    process:
      size: 1600m
  bind-host: 0.0.0.0
rest:
  bind-address: 0.0.0.0
  address: 0.0.0.0
...
```

## Clients

### Python

```shell
$ python -m virtualenv .venv
$ source .venv/Scripts/activate
$ pip install apache-flink==1.19.0
$ pip freeze > requirements.txt

$ python word_count.py
...
+I[remember'd., 1]
```

Submit PyFlink job:

```shell
# build image
$ docker build -f pyflink.Dockerfile -t pyflink .

# on jobmanager
root@e829b4e259ed:/opt/flink# bin/flink run --python devops/python/word_count.py 
Job has been submitted with JobID 906a468ac07a1a964b046fb631c955a8
root@e829b4e259ed:/opt/flink# bin/flink list -a
No running jobs.
No scheduled jobs.
---------------------- Terminated Jobs -----------------------
17.04.2024 03:41:11 : 906a468ac07a1a964b046fb631c955a8 : insert-into_default_catalog.default_database.sink (FINISHED)
--------------------------------------------------------------
```