# -*- coding: UTF-8 -*-


# 在这里写配置可以覆盖 archery/settings.py 内的配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'archery', # 数据库名称
        'USER': 'root', # 数据库用户
        'PASSWORD': 'devops+mysql', # 数据库密码 # DEPLOY_ENV
        'HOST': 'mysql', # 数据库HOST，如果是docker启动并且关联，可以使用容器名连接
        'PORT': '3306',  # 数据库端口
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", # SQL_MODE，为了兼容select * group by，可以按需调整
            'charset': 'utf8mb4'
        },
        'TEST': {
            'NAME': 'test_archery',
            'CHARSET': 'utf8mb4',
        },
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0", # redis://host:port/db # DEPLOY_ENV
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "devops+redis" # DEPLOY_ENV
        }
    }
}