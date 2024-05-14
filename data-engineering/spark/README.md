# Spark

- https://hub.docker.com/r/apache/spark
- https://hub.docker.com/r/bitnami/spark

kickoff:

```shell
docker-compose up --scale spark-worker=2 -d

# ref: https://stackoverflow.com/questions/67248234/scaling-of-docker-compose-services-results-in-port-conflict
docker compose restart
```

Access Spark Master at `http://localhost:8080/`.


```shell
I have no name!@d94518ad9289:/opt/bitnami/spark$ ls bin
beeline               find-spark-home.cmd  pyspark.cmd      spark-class          spark-shell       spark-sql.cmd     spark-submit2.cmd
beeline.cmd           load-spark-env.cmd   pyspark2.cmd     spark-class.cmd      spark-shell.cmd   spark-sql2.cmd    sparkR
docker-image-tool.sh  load-spark-env.sh    run-example      spark-class2.cmd     spark-shell2.cmd  spark-submit      sparkR.cmd
find-spark-home       pyspark              run-example.cmd  spark-connect-shell  spark-sql         spark-submit.cmd  sparkR2.cmd

# python shell
$ ./bin/pyspark
Error: pyspark does not support any application options.
# ref: https://github.com/bitnami/containers/issues/38139
$ ./bin/spark-submit pyspark-shell-main
Python 3.11.8 (main, Mar 22 2024, 12:24:25) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

# submit jobs
$ ./bin/spark-submit examples/src/main/python/pi.py 10
...
Pi is roughly 3.142720
...

# scala shell
$ ./bin/spark-shell
...
scala> 

$ bin/spark-sql 
...
spark-sql (default)> 
```