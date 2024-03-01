# MySQL

Initialize directory and files:

```shell
touch docker-compose.yml

mkdir -p data
mkdir -p conf/{conf.d,mysql.conf.d}
touch conf/conf.d/my.cnf
```

## MySQL Shell

```shell
root@localhost:/opt/mysql# docker exec -it mysql bash
bash-4.2# mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 5.7.44-log MySQL Community Server (GPL)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>

```


## Backup

```shell
# create backup directory
mkdir -p /var/lib/mysql/backup

# in container: backup data in database
mysqldump -u root -p <db> -t > /var/lib/mysql/backup/<db>-data.sql
# dump specific table
# mysqldump -u root -p <db> <table> -t > /var/lib/mysql/backup/<db>-<table>.sql
```

```shell
# in container of another side
mysql -u root -p
mysql > source /var/lib/mysql/backup/<db>-data.sql
```


## Replication

Initialize replication procedures:

```sql
-- (1) master: create repl users
mysql > CREATE USER repl_user;
mysql > GRANT REPLICATION SLAVE ON *.* TO repl_user IDENTIFIED BY '<xxx>';

-- (2) repl: 
mysql> CHANGE MASTER TO
    MASTER_HOST = '<master-host>',
    MASTER_PORT = 3306,
    MASTER_USER = 'repl_user',
    MASTER_PASSWORD = '<xxx>';
mysql> START SLAVE;

-- (3) master: backup
bash-4.2# mysqldump --host=127.0.0.1 --port=3306 --all-databases --master-data=1 -u root -p > master.sql
Enter password:
-- including: CHANGE MASTER TO MASTER_LOG_FILE='mysql-bin.000013', MASTER_LOG_POS=14269;

-- (4) repl: stop slave.
mysql> STOP SLAVE;

-- (5) master: restore to repl
bash-4.2# mysql --host=mysql-repl --port=3306 -u root -p < master.sql
Enter password:

-- (6) repl: start slave.
mysql> START SLAVE;
```

Verification:

```sql
-- on msater
CREATE TABLE `app`.`repl_test` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `field1` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin
COMMENT = 'Replication testing';

INSERT INTO `app`.`repl_test` (`field1`) VALUES ('hello, repl.');

-- on repl
SELECT * FROM app.repl_test;


-- on master
DROP TABLE IF EXISTS `app`.`repl_test`;

-- on repl
SELECT * FROM app.repl_test;
-- Error Code: 1146. Table 'app.repl_test' doesn't exist	0.188 sec
```

Do replicate from a specific Position:

```sql
-- on master
mysql> show master status;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000013 |     9581 |              |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

-- on repl
mysql> CHANGE MASTER TO
    MASTER_HOST = '<master-host>',
    MASTER_PORT = 3306,
    MASTER_USER = 'repl_user',
    MASTER_PASSWORD = '<xxx>'
    MASTER_LOG_FILE = 'mysql-bin.000013',
    MASTER_LOG_POS = 9581;
mysql> START SLAVE;
```

## Slow log

```ini
[mysqld]
# Logs
log_output=TABLE,FILE
slow_query_log=ON
slow_query_log_file=/var/lib/mysql/slow_query.log
long_query_time=1
```

```sql
-- system variables
show variables like 'long%';

-- SHOW CREATE TABLE mysql.slow_log;
SELECT event_time, CAST(argument AS CHAR) as arg FROM mysql.general_log;
SELECT start_time, CAST(sql_text AS CHAR) as sql_text FROM mysql.slow_log;

-- mock long queries
SELECT sleep(3), 'hello';
```

## TPCC

```sql
CREATE SCHEMA `test` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin ;
```

```shell
# https://github.com/Percona-Lab/sysbench-tpcc
# https://github.com/akopytov/sysbench

# (1) Prepare data and tables
./tpcc.lua \
--db-driver=mysql \
--mysql-user=root \
--mysql_password=devops+mysql \
--mysql-db=test \
--mysql-host=127.0.0.1 \
--mysql-port=3306 \
--time=300 --threads=10 --report-interval=1 --tables=1 --scale=100 \
prepare

# (2) Run
./tpcc.lua \
--db-driver=mysql \
--mysql-user=root \
--mysql_password=devops+mysql \
--mysql-db=test \
--mysql-host=127.0.0.1 \
--mysql-port=3306 \
--time=300 --threads=10 --report-interval=1 --tables=1 --scale=100 \
run

# (3) Cleanup
./tpcc.lua \
--db-driver=mysql \
--mysql-user=root \
--mysql_password=devops+mysql \
--mysql-db=test \
--mysql-host=127.0.0.1 \
--mysql-port=3306 \
--time=300 --threads=10 --report-interval=1 --tables=1 --scale=100 \
cleanup
```

## Tuning


```ini
innodb_buffer_pool_size
join_buffer_size
sort_buffer_size
innodb_sort_buffer_size
```