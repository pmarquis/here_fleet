DROP TABLE if exists fleet_positions_by_day;

CREATE TABLE fleet_positions_by_day
(
  id bigserial primary key, -- The primary key
  car_id int NOT NULL,
  day date NOT NULL
);
SELECT AddGeometryColumn('fleet_positions_by_day', 'geometry', 4326, 'LINESTRING', 2, true);

ALTER TABLE fleet_positions_by_day OWNER TO here;
