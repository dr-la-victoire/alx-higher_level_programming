-- This script lists all the rows of the second_table
-- It does not list rows without a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

