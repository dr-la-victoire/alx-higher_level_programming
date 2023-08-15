-- This script displays the average temperature
-- Its ordered by descending order
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

