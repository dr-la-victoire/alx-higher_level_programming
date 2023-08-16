-- This script creates a database for USA
-- It has a table for the states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	name VARCHAR(256) NOT NULL
	);

