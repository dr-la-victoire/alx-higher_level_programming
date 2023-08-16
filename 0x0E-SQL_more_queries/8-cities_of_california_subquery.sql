-- This script lists all the cities in Carlifornia
-- which can be found in the USA database

SELECT id, name 
FROM cities 
WHERE state_id = (
	SELECT *
	FROM states
	WHERE name = 'California');
ORDER BY id ASC;

