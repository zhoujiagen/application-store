CREATE SCHEMA `gis` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin ;

CREATE TABLE `gis` (
  `id` bigint(20) NOT NULL,
  `entity_id` varchar(100) NOT NULL COMMENT '实体ID',
  `gis` geometry NOT NULL COMMENT '位置',
  `geohash` varchar(20) GENERATED ALWAYS AS (st_geohash(`gis`,8)) VIRTUAL,
  PRIMARY KEY (`id`),
  SPATIAL KEY `idx_gis` (`gis`),
  KEY `idx_entity` (`entity_id`),
  KEY `idx_geohash` (`geohash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='GIS';

-- testing functions
SELECT t.p, ST_AsText(t.p)
FROM
(
select ST_GeomFromText('point(0 0)') AS p
UNION
select ST_GeomFromText('point(3 4)') AS p
) AS t;

SELECT ST_Distance(point(0, 0), point(3, 4)); -- 5
SELECT ST_Distance_Sphere(point(0, 0), point(3, 4)); -- 555810.7203217451

-- 29.36 （米）
-- 29.379066293341957
SELECT ST_Distance_Sphere(
   POINT(114.914698,34.774211), 
   POINT(114.9145036,34.7740005)
);

-- populate data
INSERT INTO gis(entity_id,gis)
VALUES
('aaa', ST_GeomFromText('POINT(114.914698 34.774211)')),
('bbb', ST_GeomFromText('POINT(114.9145036 34.7740005)'));

-- calculate distance
SELECT entity_id, gis, ST_AsText(gis), geohash FROM gis.gis;
SELECT ST_Distance_Sphere(
	(SELECT gis FROM gis.gis WHERE entity_id = 'aaa'),
    (SELECT gis FROM gis.gis WHERE entity_id = 'bbb')
) AS distance;

SELECT g.id, g.entity_id, g.gis, ST_AsText(g.gis), g.geohash, 
	ST_Distance_Sphere(g.gis, (SELECT gis FROM gis.gis WHERE entity_id = 'aaa')) AS distance
FROM gis.gis AS g
WHERE ST_Distance_Sphere(g.gis, (SELECT gis FROM gis.gis WHERE entity_id = 'aaa')) < 30
AND g.entity_id != 'aaa';

SELECT ST_LatFromGeoHash(v.h), ST_LongFromGeoHash(v.h), ST_PointFromGeoHash(v.h, 8)
FROM
(
SELECT ST_GeoHash(Point(0,1), 8) AS h
) AS v
