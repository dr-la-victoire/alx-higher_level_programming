-- This script counts the number of shows of each
-- genre in the movie database

SELECT tv_genres.name AS 'genre', COUNT(tv_shows.title) AS 'number_of_shows'
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY 'number_of_shows' DESC;

