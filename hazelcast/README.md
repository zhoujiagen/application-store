# Hazelcast

- https://hazelcast.com/

## Docker Deployment

> 192.168.3.131: local host ip
> hz-cluster: cluster name

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
http://localhost:18080/

hz-cluster
192.168.3.131:5701,192.168.3.131:5702
```

## CDC

1. Setup check

Member library:

```shell
# hz-mem1
$ pwd
/opt/hazelcast/lib
$ ls | grep cdc
hazelcast-jet-cdc-debezium-5.3.6.jar
hazelcast-jet-cdc-mysql-5.3.6.jar
hazelcast-jet-cdc-postgres-5.3.6.jar
```

MySQL datas:

```shell
# hz-debezium-mysql
# mysql -u debezium -p
Enter password: dbz
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| inventory          |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use inventory;
Database changed
mysql> show tables;
+---------------------+
| Tables_in_inventory |
+---------------------+
| addresses           |
| customers           |
| geom                |
| orders              |
| products            |
| products_on_hand    |
+---------------------+
6 rows in set (0.00 sec)
mysql> select * from customers;
+------+------------+-----------+-----------------------+
| id   | first_name | last_name | email                 |
+------+------------+-----------+-----------------------+
| 1001 | Sally      | Thomas    | sally.thomas@acme.com |
| 1002 | George     | Bailey    | gbailey@foobar.com    |
| 1003 | Edward     | Walker    | ed@walker.com         |
| 1004 | Anne       | Kretchmar | annek@noanswer.org    |
+------+------------+-----------+-----------------------+
4 rows in set (0.00 sec)
```

Submit job:

```shell
# hz-mem1
$ bin/hz-cli -t hz-cluster@192.168.3.131:5701 submit apps/hazelcast-cdc-mysql/target/hazelcast-cdc-mysql-1.0-SNAPSHOT.jar
```

HZ SQL or HZ CLI:

```shell
# hz-mem1
$ bin/hz-cli -t hz-cluster@192.168.3.131:5701 list-jobs
ID                  STATUS             SUBMISSION TIME         NAME
0b5a-1707-5240-0004 RUNNING            2024-03-07T05:26:35.749 mysql-monitor
# or
$ bin/hz-cli -t hz-cluster@192.168.3.131:5701 sql
sql> show jobs;
+--------------------+
|name                |
+--------------------+
|mysql-monitor       |
+--------------------+
1 row(s) selected

$ bin/hz-cli -t hz-cluster@192.168.3.131:5701 console
hazelcast[default] > ns customers
namespace: customers
hazelcast[customers] > m.entries
1002: Customer {id=1002, firstName=George, lastName=Bailey, email=gbailey@foobar.com}
1003: Customer {id=1003, firstName=Edward, lastName=Walker, email=ed@walker.com}
1004: Customer {id=1004, firstName=Anne, lastName=Kretchmar, email=annek@noanswer.org}
1001: Customer {id=1001, firstName=Sally, lastName=Thomas, email=sally.thomas@acme.com}
Total 4
```

2. Update MySQL and view changes

```shell
# hz-debezium-mysql
mysql> UPDATE customers SET first_name='Anne Marie' WHERE id=1004;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0
# hz-mem1
hazelcast[customers] > m.entries
1002: Customer {id=1002, firstName=George, lastName=Bailey, email=gbailey@foobar.com}
1003: Customer {id=1003, firstName=Edward, lastName=Walker, email=ed@walker.com}
1004: Customer {id=1004, firstName=Anne Marie, lastName=Kretchmar, email=annek@noanswer.org}   <--
1001: Customer {id=1001, firstName=Sally, lastName=Thomas, email=sally.thomas@acme.com}
Total 4

# hz-debezium-mysql
mysql> UPDATE customers SET email='edward.walker@walker.com' WHERE id=1003;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0
# hz-mem1
hazelcast[customers] > m.entries
1002: Customer {id=1002, firstName=George, lastName=Bailey, email=gbailey@foobar.com}
1003: Customer {id=1003, firstName=Edward, lastName=Walker, email=edward.walker@walker.com}     <--
1004: Customer {id=1004, firstName=Anne Marie, lastName=Kretchmar, email=annek@noanswer.org}
1001: Customer {id=1001, firstName=Sally, lastName=Thomas, email=sally.thomas@acme.com}
Total 4
```

3. Cleanup

Cancel job and clean map:

```shell
# hz-mem1
$ bin/hz-cli -t hz-cluster@192.168.3.131:5701 cancel mysql-monitor
Cancelling job id=0b5a-1707-5240-0004, name=mysql-monitor, submissionTime=2024-03-07T05:26:35.749
Job cancelled. 

hazelcast[customers] > m.destroy
Destroyed!
```