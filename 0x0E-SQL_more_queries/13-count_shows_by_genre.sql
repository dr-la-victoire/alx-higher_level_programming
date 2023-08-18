-- This script counts the number of shows of each
-- genre in the movie database

SELECT tv_genres.name AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

