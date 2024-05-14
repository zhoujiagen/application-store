# ClickHouse

- https://hub.docker.com/r/clickhouse/clickhouse-server/

```shell
# prepare
docker volume create clickhouse
docker volume create clickhouse-logs
```

Inspect container contents:

```shell
root@82c2e06287c6:/# cat entrypoint.sh
...
exec /usr/bin/clickhouse su "${USER}:${GROUP}" /usr/bin/clickhouse-server --config-file="$CLICKHOUSE_CONFIG" "$@"
...
root@82c2e06287c6:/# echo $CLICKHOUSE_CONFIG
/etc/clickhouse-server/config.xml
```

Access `http://localhost:8123/play` to play, `http://localhost:8123/dashboard` to view bashboard.

```
# dashboard error
Code: 456. DB::Exception: Query parameter `rounding` was not set. (UNKNOWN_QUERY_PARAMETER) (version 24.3.2.23 (official build))
```

## Clients

### Bytebase

Access bytebase through `http://localhost:18080`.

```
# create account
devops@example.com
devops+bytebase
```

### `clickhouse-client`

- StripeLog

An example from '10. Analytics-on-read' in 'Event Streams in Action'.


```shell
# in container
# load data
root@87d4977e7f57:/var/lib/clickhouse/user_files# ls
clickhouse-events_reference.sql  clickhouse-events_view.sql clickhouse-events.sql  events.ndjson  mysql-events_reference.sql
root@87d4977e7f57:/var/lib/clickhouse/user_files# clickhouse-client --queries-file clickhouse-events.sql

root@87d4977e7f57:/var/lib/clickhouse/user_files# clickhouse-client -q "SELECT * FROM devops.events LIMIT 1"
TRUCK_DEPARTS2018-12-01 03:24:00false751.522834-0.081813323391HGCM82633A004352

root@87d4977e7f57:/var/lib/clickhouse/user_files# wc -l events.ndjson 
130 events.ndjson
root@87d4977e7f57:/var/lib/clickhouse/user_files# clickhouse-client -q "SELECT COUNT(*) FROM devops.events"
130

# reference tables in MySQL
root@e0db43f92964:/var/lib/clickhouse/user_files# clickhouse-client --queries-file clickhouse-events_reference.sql 
root@e0db43f92964:/var/lib/clickhouse/user_files# clickhouse-client -q "SELECT * FROM devops.customers"
b39a2b30-049b-436a-a45d-46d290df65d3    Karl    99501
4594f1a1-a7a2-4718-bfca-6e51e73cc3e7    Maria   72217-2517
b1e5d874-963b-4992-a232-4679438261ab    Amit    90089

# JOIN tables
root@e0db43f92964:/var/lib/clickhouse/user_files# clickhouse-client -q 'SELECT e.event, e.timestamp, e."vehicle.vin", v.* FROM devops.events AS e LEFT JOIN devops.vehicles AS v ON e."vehicle.vin" = v.vin LIMIT 1;'
TRUCK_DEPARTS   2018-12-01 03:24:00     1HGCM82633A004352       1HGCM82633A004352       Ford    Transit 2005

# Views
root@e0db43f92964:/var/lib/clickhouse/user_files# clickhouse-client --queries-file clickhouse-views.sql 
DRIVER_MISSES_CUSTOMER  2018-12-10 21:53:00     4594f1a1-a7a2-4718-bfca-6e51e73cc3e7    false   Maria   72217-2517      c4b843f2-0ef6-4666-8f8d-91ac2e366571          Andreas 1994-03-13      51.4972997      -0.0955459      102     14a714cf-5a89-417e-9c00-f2dba0d1844d    894             0            0
root@e0db43f92964:/var/lib/clickhouse/user_files# 
```

### Python

- https://clickhouse.com/docs/en/integrations/python

> The official ClickHouse Connect Python driver uses HTTP protocol for communication with the ClickHouse server.

errors:

```shell
clickhouse_connect.driver.exceptions.DatabaseError: :HTTPDriver for http://localhost:8123 returned response code 500)
 std::exception. Code: 1001, type: std::__1::__fs::filesystem::filesystem_error, e.what() = filesystem error: in rename: Permission denied ["/var/lib/clickhouse/store/eab/eabb7d67-5338-45c1-ae2a-1c554a431753/tmp_insert_all_1_1_0/"] ["/var/lib/clickhouse/store/eab/eabb7d67-5338-45c1-ae2a-1c554a431753/all_1_1_0/"]
Cannot print extra info for Poco::Exception (version 24.3.2.23 (official build))

# workardound ref: https://github.com/ClickHouse/ClickHouse/issues/35036
```

```shell
$ python ex_clickhouse.py 
[(2000, -50.9035)]
```