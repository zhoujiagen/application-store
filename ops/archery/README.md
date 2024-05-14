# Archery

- https://github.com/hhyo/Archery


```shell
docker network create ops-network
#启动
docker-compose -f docker-compose.yml up -d

#表结构初始化
docker exec -ti archery bash
cd /opt/archery
source /opt/venv4archery/bin/activate
python3 manage.py makemigrations sql
python3 manage.py migrate

#数据初始化
python3 manage.py dbshell<sql/fixtures/auth_group.sql
python3 manage.py dbshell<src/init_sql/mysql_slow_query_review.sql

#创建管理用户
python3 manage.py createsuperuser
```

## FIX

- `archery/custom/archiver.py`: 修复数据库归档时最后一行未归档问题.
- `archery/custom/mongo.py`: 修复MongoDB语法解析时按`;`拆分语句情况下字段中存在`;`问题.

## TODO

- [x] SQL检测规则配置
