# sysbench

- https://github.com/akopytov/sysbench

```shell
cd docker
docker build -t dev/sysbench .
docker container cp sysbench:/usr/share/sysbench/ lua
```

```sql
CREATE DATABASE sysbench;
CREATE USER 'sysbench'@'%' IDENTIFIED BY 'sysbench';
GRANT ALL PRIVILEGES ON sysbench.* TO 'sysbench'@'%';
```

TPCC

```
git clone https://github.com/Percona-Lab/sysbench-tpcc.git
```