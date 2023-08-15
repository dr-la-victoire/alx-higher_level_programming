-- This script displays the highest temperatures
-- in July and August
-- descending order
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
WHERE month = 'July' AND month = 'August'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

