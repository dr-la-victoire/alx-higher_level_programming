-- This script displays the highest temperatures
-- in July and August
-- descending order
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

