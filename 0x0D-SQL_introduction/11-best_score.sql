-- This script lists all the best scores in
-- the second table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
