CREATE TABLE devops.log
(
    `ip` String,
    `time` Datetime,
    `url` String,
    `status` UInt8,
    `size` UInt32,
    `agent` String
)
ENGINE = MergeTree
ORDER BY date(time);