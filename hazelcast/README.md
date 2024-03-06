# Hazelcast

- https://hazelcast.com/

Local cluster with docker:

```shell
docker run --rm --name member1 -e HZ_NETWORK_PUBLICADDRESS=192.168.3.131:5701 -p 5701:5701 hazelcast/hazelcast:5.3.6
docker run --rm --name member2 -e HZ_NETWORK_PUBLICADDRESS=192.168.3.131:5702 -p 5702:5701 hazelcast/hazelcast:5.3.6
```

Local cluster with docker compose:

```shell
docker compose ps
NAME                IMAGE                       COMMAND             SERVICE             CREATED             STATUS                    PORTS
hz-mem1             hazelcast/hazelcast:5.3.6   "hz start"          hz-mem1             17 seconds ago      Up 16 seconds (healthy)   192.168.3.131:5701->5701/tcp
hz-mem2             hazelcast/hazelcast:5.3.6   "hz start"          hz-mem2             17 seconds ago      Up 16 seconds (healthy)   192.168.3.131:5702->5701/tcp
```

Management Center:

```
hz-cluster
192.168.3.131:5701,192.168.3.131:5702
```