-- Example from "Cassandra: The Definitive Guide" Chapter 4

USE my_keyspace;

CREATE TABLE user ( first_name text, last_name text, title text, PRIMARY KEY (last_name, first_name)) ;

INSERT INTO user (first_name, last_name) VALUES ('Mary', 'Rodriguez');
SELECT * FROM user WHERE last_name='Rodriguez';

ALTER TABLE user ADD middle_initial text;


