#-*-coding: UTF-8 -*-

import sqlalchemy
from testcontainers.mysql import MySqlContainer

if __name__=="__main__":
  with MySqlContainer('mysql:8.0.36') as mysql:
      engine = sqlalchemy.create_engine(mysql.get_connection_url())
      with engine.begin() as connection:
          result = connection.execute(sqlalchemy.text("select version()"))
          version, = result.fetchone()
          print(version)