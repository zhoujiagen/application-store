# Hadoop

- https://hub.docker.com/r/apache/hadoop


Namenode UI: http://localhost:9870/

ResourceManager UI: http://localhost:8088/

```
# in container
bash-4.2$ pwd
/opt/hadoop
bash-4.2$ ls share/hadoop/mapreduce
hadoop-mapreduce-client-app-3.3.6.jar     hadoop-mapreduce-client-hs-plugins-3.3.6.jar       hadoop-mapreduce-client-shuffle-3.3.6.jar   lib-examples
hadoop-mapreduce-client-common-3.3.6.jar  hadoop-mapreduce-client-jobclient-3.3.6-tests.jar  hadoop-mapreduce-client-uploader-3.3.6.jar  sources
hadoop-mapreduce-client-core-3.3.6.jar    hadoop-mapreduce-client-jobclient-3.3.6.jar        hadoop-mapreduce-examples-3.3.6.jar
hadoop-mapreduce-client-hs-3.3.6.jar      hadoop-mapreduce-client-nativetask-3.3.6.jar       jdiff

bash-4.2$ yarn jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar pi 10 15
...
Job Finished in 19.04 seconds
Estimated value of Pi is 3.17333333333333333333
```