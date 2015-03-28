DROP TABLE if exists fleet_positions;

CREATE TABLE fleet_positions
(
  id bigserial primary key, -- The primary key
  car_id int NOT NULL,
  logdate timestamp NOT NULL,
  position geometry(Point, 4326) NOT NULL
);

ALTER TABLE fleet_positions OWNER TO here;