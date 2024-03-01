SELECT * FROM system_schema.keyspaces
SELECT * FROM system_schema.tables WHERE keyspace_name = 'my_keyspace'
SELECT * FROM system_schema.columns WHERE keyspace_name = 'my_keyspace' AND table_name = 'user';
SELECT * FROM system_schema.indexes WHERE keyspace_name = 'my_keyspace' AND table_name = 'user';
SELECT * FROM system_schema.aggregates WHERE keyspace_name = 'my_keyspace'
SELECT * FROM system_schema.functions WHERE keyspace_name = 'my_keyspace'
SELECT * FROM system_schema.triggers WHERE keyspace_name = 'my_keyspace'
SELECT * FROM system_schema.types WHERE keyspace_name = 'my_keyspace'
SELECT * FROM system_schema.views WHERE keyspace_name = 'my_keyspace'