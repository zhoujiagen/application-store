# https://medium.com/@chachia.mohamed/stress-testing-in-centos-using-sysbench-and-stress-commands-2c4530122c45
# sysbench --db-driver=mysql --mysql-host=mysql --mysql-user=sysbench --mysql-password=sysbench --mysql-db=sysbench --tables=2 --table-size=100  /usr/share/sysbench/oltp_read_write.lua prepare
# sysbench --db-driver=mysql --mysql-host=mysql --mysql-user=sysbench --mysql-password=sysbench --mysql-db=sysbench --tables=2 --table-size=100 --num-threads=2 --max-time=30  /usr/share/sysbench/oltp_read_write.lua run

# https://github.com/Percona-Lab/sysbench-tpcc
# ./tpcc.lua --mysql-socket=/tmp/mysql.sock --mysql-user=root --mysql-db=sbt --time=300 --threads=64 --report-interval=1 --tables=10 --scale=100 --db-driver=mysql prepare
# ./tpcc.lua --mysql-socket=/tmp/mysql.sock --mysql-user=root --mysql-db=sbt --time=300 --threads=64 --report-interval=1 --tables=10 --scale=100 --db-driver=mysql run
# ./tpcc.lua --mysql-socket=/tmp/mysql.sock --mysql-user=root --mysql-db=sbt --time=300 --threads=64 --report-interval=1 --tables=10 --scale=100 --db-driver=mysql cleanup
export DB_CONNECT="--db-driver=mysql --mysql-host=mysql --mysql-user=sysbench --mysql-password=sysbench --mysql-db=sysbench"
sysbench $DB_CONNECT /usr/share/sysbench/tpcc.lua --time=30 --threads=2 --report-interval=1 --tables=2 --scale=100 --db-driver=mysql prepare
sysbench $DB_CONNECT /usr/share/sysbench/tpcc.lua --time=30 --threads=2 --report-interval=1 --tables=2 --scale=100 --db-driver=mysql run

