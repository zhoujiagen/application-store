// DESCRIBE CLUSTER;

// SHOW VERSION;

CREATE KEYSPACE my_keyspace WITH replication = {'class':  'SimpleStrategy', 'replication_factor': 1};

DESCRIBE KEYSPACE my_keyspace;

USE my_keyspace;

CREATE TABLE user ( first_name text, last_name text, title text, PRIMARY KEY (last_name, first_name)) ;

DESCRIBE TABLE user;

INSERT INTO user (first_name, last_name, title) VALUES ('Bill', 'Nguyen', 'Mr.');


SELECT * FROM user WHERE first_name='Bill' AND last_name='Nguyen';
SELECT * FROM user where last_name = 'Nguyen';
SELECT * FROM user where first_name = 'Bill';
SELECT COUNT (*) FROM user;

DELETE title FROM USER WHERE first_name='Bill' AND last_name='Nguyen';
SELECT * FROM user WHERE first_name='Bill' AND last_name='Nguyen';

DELETE FROM USER WHERE first_name='Bill' AND last_name='Nguyen';
SELECT * FROM user WHERE first_name='Bill' AND last_name='Nguyen';

DROP TABLE user;