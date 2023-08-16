-- This script counts the number of shows of each
-- genre in the movie database

SELECT tv_show_genres.name AS 'genre', COUNT(tv_shows.title) AS 'number_of_shows'
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY 'number_of_shows' DESC;

