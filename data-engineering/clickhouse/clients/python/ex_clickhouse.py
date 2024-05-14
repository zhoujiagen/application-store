#-*-coding: UTF-8 -*-

import clickhouse_connect

if __name__=="__main__":
  client = clickhouse_connect.get_client(
    host='localhost', 
    database='devops',
    username='devops', 
    password='devops+clickhouse')
  
  drop_table_sql = "DROP TABLE IF EXISTS devops.new_table"
  client.command(drop_table_sql)
  
  create_table_sql = """
  CREATE TABLE IF NOT EXISTS devops.new_table (
    key UInt32, 
    value String, 
    metric Float64) 
  ENGINE MergeTree 
  ORDER BY key"""
  client.command(create_table_sql)

  row1 = [1000, 'String Value 1000', 5.233]
  row2 = [2000, 'String Value 2000', -107.04]
  data = [row1, row2]
  client.insert(table='devops.new_table', data=data, column_names=['key', 'value', 'metric'])

  result = client.query('SELECT max(key), avg(metric) FROM new_table')
  print(result.result_rows)


