# -*- coding: utf-8 -*

import pymysql
from prettytable import from_db_cursor

_DEBUG = False


def open_connection(
        host="127.0.0.1",
        username="root",
        password="admin",
        database="test"):
    """获取数据库连接"""
    return pymysql.connect(host, username, password, database)


def close_connection(conn):
    """关闭数据库连接."""
    conn.close()


def execute_sql_in_trx(conn, sql):
    """在事务中执行SQL"""

    if _DEBUG:
        print("execute sql:\n{}\n".format(sql))

    try:
        conn.cursor().execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
        raise e


def execute_query(conn, sql):
    """执行查询, 并展示."""

    if _DEBUG:
        print("execute sql:\n{}\n".format(sql))

    cursor = conn.cursor()
    cursor.execute(sql)
    print(from_db_cursor(cursor))


def execute_query_and_fetch_result(conn, sql):
    """执行查询, 获取结果."""

    if _DEBUG:
        print("execute sql:\n{}\n".format(sql))

    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        if _DEBUG:
            print("execute sql failed:\n{}\n, {}".format(sql, e))
        raise e
