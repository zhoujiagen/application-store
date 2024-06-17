# Apache Iceberg
- https://iceberg.apache.org/

## Spark
- https://iceberg.apache.org/spark-quickstart/#spark-and-iceberg-quickstart

```shell
# spark-sql
spark-sql ()> CREATE TABLE demo.nyc.taxis
            > (
            >   vendor_id bigint,
            >   trip_id bigint,
            >   trip_distance float,
            >   fare_amount double,
            >   store_and_fwd_flag string
            > )
            > PARTITIONED BY (vendor_id);
Time taken: 2.152 seconds
spark-sql ()> INSERT INTO demo.nyc.taxis
            > VALUES (1, 1000371, 1.8, 15.32, 'N'), (2, 1000372, 2.5, 22.15, 'N'), (2, 1000373, 0.9, 9.01, 'N'), (1, 1000374, 8.4, 42.13, 'Y');
Time taken: 3.499 seconds
spark-sql ()> SELECT * FROM demo.nyc.taxis;
1       1000371 1.8     15.32   N
1       1000374 8.4     42.13   Y
2       1000372 2.5     22.15   N
2       1000373 0.9     9.01    N
Time taken: 0.731 seconds, Fetched 4 row(s)
```

```shell
spark-sql ()> show catalogs;
demo
spark_catalog
Time taken: 0.035 seconds, Fetched 2 row(s)
spark-sql ()> show databases;
nyc
Time taken: 0.039 seconds, Fetched 1 row(s)
spark-sql ()> use nyc;
Time taken: 0.058 seconds
spark-sql (nyc)> show tables;
taxis
Time taken: 0.119 seconds, Fetched 1 row(s) 
spark-sql (nyc)> describe taxis;
vendor_id               bigint                                      
trip_id                 bigint                                      
trip_distance           float                                       
fare_amount             double                                      
store_and_fwd_flag      string                                      
# Partition Information                                             
# col_name              data_type               comment             
vendor_id               bigint                                      
Time taken: 0.221 seconds, Fetched 8 row(s)
```