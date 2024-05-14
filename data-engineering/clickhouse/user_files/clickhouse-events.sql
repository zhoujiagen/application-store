CREATE TABLE IF NOT EXISTS devops.events
(
  "event" VARCHAR(23) NOT NULL,
  "timestamp" TIMESTAMP NOT NULL,
  "customer.id" CHAR(36),
  "customer.is_vip" BOOLEAN,
  "employee.id" CHAR(36),
  "employee.job_role" VARCHAR(12),
  "location.elevation" SMALLINT,
  "location.latitude" DOUBLE PRECISION,
  "location.longitude" DOUBLE PRECISION,
  "package.id" CHAR(36),
  "vehicle.mileage" INT,
  "vehicle.vin" CHAR(17)
) ENGINE = StripeLog;


-- ref: https://clickhouse.com/docs/en/integrations/data-formats/json
SET date_time_input_format = 'best_effort';
SET input_format_import_nested_json = 1;

-- testing
-- SELECT * 
-- FROM file('events.ndjson', JSONEachRow, '`event` String, `timestamp` DateTime, `customer.id` String, `customer.is_vip` Bool, `employee.id` String, `employee.job_role` String, `location.elevation` Int16, `location.latitude` Float64, `location.longitude` Float64, `package.id` String, `vehicle.mileage` Int32, `vehicle.vin` String') 
-- LIMIT 1;

INSERT INTO devops.events
FROM INFILE 'events.ndjson' FORMAT JSONEachRow
;