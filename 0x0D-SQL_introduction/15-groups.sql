-- This script lists the number of records with the same score
-- In the table second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

