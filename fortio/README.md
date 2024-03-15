# Fortio
- https://github.com/fortio/fortio

Access Server `fortio-server`: http://localhost:18080/fortio/

Sample output of `fortio-loader`:

```shell
2024-03-15 14:47:00 Aggregated Sleep Time : count 8 avg -3.6833207 +/- 1.231 min -4.916709174 max -2.451522061 sum -29.4665655
2024-03-15 14:47:00 # range, mid point, percentile, count
2024-03-15 14:47:00 >= -4.91671 <= -2.45152 , -3.68412 , 100.00, 8
2024-03-15 14:47:00 # target 50% -3.8602
2024-03-15 14:47:00 WARNING 100.00% of sleep were falling behind
2024-03-15 14:47:00 Aggregated Function Time : count 8 avg 3.0125075 +/- 0.004809 min 3.006843669 max 3.018966264 sum 24.1000603
2024-03-15 14:47:00 # range, mid point, percentile, count
2024-03-15 14:47:00 >= 3.00684 <= 3.01897 , 3.0129 , 100.00, 8
2024-03-15 14:47:00 # target 50% 3.01204
2024-03-15 14:47:00 # target 75% 3.0155
2024-03-15 14:47:00 # target 90% 3.01758
2024-03-15 14:47:00 # target 99% 3.01883
2024-03-15 14:47:00 # target 99.9% 3.01895
2024-03-15 14:47:00 Error cases : no data
2024-03-15 14:47:00 # Socket and IP used for each connection:
2024-03-15 14:47:00 [0]   3 socket used, resolved to 192.168.3.134:5001, connection timing : count 3 avg 0.0037549663 +/- 0.001674 min 0.001988639 max 0.006003377 sum 0.011264899
2024-03-15 14:47:00 [1]   3 socket used, resolved to 192.168.3.134:5001, connection timing : count 3 avg 0.003507406 +/- 0.001664 min 0.002095474 max 0.005844004 sum 0.010522218
2024-03-15 14:47:00 [2]   3 socket used, resolved to 192.168.3.134:5001, connection timing : count 3 avg 0.0034241607 +/- 0.001716 min 0.002198151 max 0.005850237 sum 0.010272482
2024-03-15 14:47:00 [3]   3 socket used, resolved to 192.168.3.134:5001, connection timing : count 3 avg 0.0040882833 +/- 0.002067 min 0.002077645 max 0.006931294 sum 0.01226485
2024-03-15 14:47:00 Connection time histogram (s) : count 12 avg 0.0036937041 +/- 0.001807 min 0.001988639 max 0.006931294 sum 0.044324449
2024-03-15 14:47:00 # range, mid point, percentile, count
2024-03-15 14:47:00 >= 0.00198864 <= 0.002 , 0.00199432 , 8.33, 1
2024-03-15 14:47:00 > 0.002 <= 0.003 , 0.0025 , 50.00, 5
2024-03-15 14:47:00 > 0.003 <= 0.004 , 0.0035 , 66.67, 2
2024-03-15 14:47:00 > 0.005 <= 0.006 , 0.0055 , 83.33, 2
2024-03-15 14:47:00 > 0.006 <= 0.00693129 , 0.00646565 , 100.00, 2
2024-03-15 14:47:00 # target 50% 0.003
2024-03-15 14:47:00 # target 75% 0.0055
2024-03-15 14:47:00 # target 90% 0.00637252
2024-03-15 14:47:00 # target 99% 0.00687542
2024-03-15 14:47:00 # target 99.9% 0.00692571
2024-03-15 14:47:00 Sockets used: 12 (for perfect keepalive, would be 4)
2024-03-15 14:47:00 Uniform: false, Jitter: false, Catchup allowed: true
2024-03-15 14:47:00 IP addresses distribution:
2024-03-15 14:47:00 192.168.3.134:5001: 12
2024-03-15 14:47:00 Code 200 : 8 (100.0 %)
2024-03-15 14:47:00 Response Header Sizes : count 8 avg 165 +/- 0 min 165 max 165 sum 1320
2024-03-15 14:47:00 Response Body/Total Sizes : count 8 avg 198 +/- 0 min 198 max 198 sum 1584
2024-03-15 14:47:00 All done 8 calls (plus 4 warmup) 3012.508 ms avg, 1.3 qps
```