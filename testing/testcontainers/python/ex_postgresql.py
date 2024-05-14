#-*-coding: UTF-8 -*-

from testcontainers.postgres import PostgresContainer
import sqlalchemy

if __name__=="__main__":
  with PostgresContainer("postgres:16.2") as postgres:
      psql_url = postgres.get_connection_url()
      engine = sqlalchemy.create_engine(psql_url)
      with engine.begin() as connection:
          version, = connection.execute(sqlalchemy.text("SELECT version()")).fetchone()
          print(version)