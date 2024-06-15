# Redis
- https://hub.docker.com/_/redis

## Single Instance

```shell
# redis-cli
127.0.0.1:6379> set foo bar
OK
127.0.0.1:6379> get foo
"bar"
127.0.0.1:6379> 
```

## Cluster
- https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/#create-a-redis-cluster
- https://github.com/redis/redis/tree/unstable/utils/create-cluster

```shell
# redis-cli --cluster create redis-7000:7000 redis-7001:7001 \
  redis-7002:7002 redis-7003:7003 redis-7004:7004 redis-7005:7005 \
  --cluster-replicas 1
>>> Performing hash slots allocation on 6 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
Adding replica redis-7004:7004 to redis-7000:7000
Adding replica redis-7005:7005 to redis-7001:7001
Adding replica redis-7003:7003 to redis-7002:7002
M: ca757d593c1e04af21a6c1e0145513f72335fbf3 redis-7000:7000
   slots:[0-5460] (5461 slots) master
M: 572a1ce3ad591f866255966ea28547d6367a4848 redis-7001:7001
   slots:[5461-10922] (5462 slots) master
M: 04517c0a0f5ddff255ef6ca7ab7473cf81c9c4cc redis-7002:7002
   slots:[10923-16383] (5461 slots) master
S: cde0538d827b2de5dd7265c71676314bc151cdef redis-7003:7003
   replicates 04517c0a0f5ddff255ef6ca7ab7473cf81c9c4cc
S: 6fe234d210425649b75499c4c7203929c2816e25 redis-7004:7004
   replicates ca757d593c1e04af21a6c1e0145513f72335fbf3
S: feef4c1f7de49092c926f1a94da6924581f3dbba redis-7005:7005
   replicates 572a1ce3ad591f866255966ea28547d6367a4848
Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
.
>>> Performing Cluster Check (using node redis-7000:7000)
M: ca757d593c1e04af21a6c1e0145513f72335fbf3 redis-7000:7000
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
M: 04517c0a0f5ddff255ef6ca7ab7473cf81c9c4cc 172.18.0.2:7002
   slots:[10923-16383] (5461 slots) master
   1 additional replica(s)
S: cde0538d827b2de5dd7265c71676314bc151cdef 172.18.0.5:7003
   slots: (0 slots) slave
   replicates 04517c0a0f5ddff255ef6ca7ab7473cf81c9c4cc
S: 6fe234d210425649b75499c4c7203929c2816e25 172.18.0.6:7004
   slots: (0 slots) slave
   replicates ca757d593c1e04af21a6c1e0145513f72335fbf3
M: 572a1ce3ad591f866255966ea28547d6367a4848 172.18.0.3:7001
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
S: feef4c1f7de49092c926f1a94da6924581f3dbba 172.18.0.4:7005
   slots: (0 slots) slave
   replicates 572a1ce3ad591f866255966ea28547d6367a4848
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```

```shell
# redis-cli -c -p 7000
127.0.0.1:7000> set foo bar
-> Redirected to slot [12182] located at 172.18.0.2:7002
OK
172.18.0.2:7002> set hello world
-> Redirected to slot [866] located at 172.18.0.7:7000
OK
172.18.0.7:7000> get foo
-> Redirected to slot [12182] located at 172.18.0.2:7002
"bar"
172.18.0.2:7002> get hello
-> Redirected to slot [866] located at 172.18.0.7:7000
"world"
172.18.0.7:7000> 
```

```shell
# redis-cli -c -p 7000               
127.0.0.1:7000> cluster help
...
127.0.0.1:7000> cluster nodes
04517c0a0f5ddff255ef6ca7ab7473cf81c9c4cc 172.18.0.2:7002@17002 master - 0 1718459226451 3 connected 10923-16383
cde0538d827b2de5dd7265c71676314bc151cdef 172.18.0.5:7003@17003 slave 04517c0a0f5ddff255ef6ca7ab7473cf81c9c4cc 0 1718459226049 3 connected
6fe234d210425649b75499c4c7203929c2816e25 172.18.0.6:7004@17004 slave ca757d593c1e04af21a6c1e0145513f72335fbf3 0 1718459227458 1 connected
ca757d593c1e04af21a6c1e0145513f72335fbf3 172.18.0.7:7000@17000 myself,master - 0 1718459226000 1 connected 0-5460
572a1ce3ad591f866255966ea28547d6367a4848 172.18.0.3:7001@17001 master - 0 1718459227000 2 connected 5461-10922
feef4c1f7de49092c926f1a94da6924581f3dbba 172.18.0.4:7005@17005 slave 572a1ce3ad591f866255966ea28547d6367a4848 0 1718459227960 2 connected
```