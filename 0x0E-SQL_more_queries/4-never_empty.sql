-- This script creates the table
-- id_not_null in the server

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1 NOT NULL,
	name VARCHAR(256)
);
