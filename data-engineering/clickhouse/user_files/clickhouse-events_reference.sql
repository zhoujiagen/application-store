CREATE TABLE IF NOT EXISTS devops.vehicles
(
  vin CHAR(17) NOT NULL,
  make VARCHAR(32) NOT NULL,
  model VARCHAR(32) NOT NULL,
  year SMALLINT
) ENGINE = MySQL('mysql:3306', 'devops', 'vehicles', 'root', 'change_me')
SETTINGS
     connection_pool_size=16, 
     connection_max_tries=3, 
     connection_wait_timeout=5, 
     connection_auto_close=true, 
     connect_timeout=10, 
     read_write_timeout=300 
;

CREATE TABLE IF NOT EXISTS devops.employees
(
  id CHAR(36) NOT NULL,
  name VARCHAR(32) NOT NULL,
  dob DATE NOT NULL
) ENGINE = MySQL('mysql:3306', 'devops', 'employees', 'root', 'change_me')
SETTINGS
     connection_pool_size=16, 
     connection_max_tries=3, 
     connection_wait_timeout=5, 
     connection_auto_close=true, 
     connect_timeout=10, 
     read_write_timeout=300 
;

CREATE TABLE IF NOT EXISTS devops.packages
(
  id CHAR(36) NOT NULL, 
  weight INT NOT NULL
) ENGINE = MySQL('mysql:3306', 'devops', 'packages', 'root', 'change_me')
SETTINGS
     connection_pool_size=16, 
     connection_max_tries=3, 
     connection_wait_timeout=5, 
     connection_auto_close=true, 
     connect_timeout=10, 
     read_write_timeout=300 
;

CREATE TABLE IF NOT EXISTS devops.customers
(
  id CHAR(36) NOT NULL,
  name VARCHAR(32) NOT NULL,
  zip_code VARCHAR(10) NOT NULL
) ENGINE = MySQL('mysql:3306', 'devops', 'customers', 'root', 'change_me')
SETTINGS
     connection_pool_size=16, 
     connection_max_tries=3, 
     connection_wait_timeout=5, 
     connection_auto_close=true, 
     connect_timeout=10, 
     read_write_timeout=300 
;