-- This script lists all the cities of California
-- The cities are found in the USA database

SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;

