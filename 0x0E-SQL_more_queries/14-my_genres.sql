-- This script lists all the genres
-- of the shlw Dexter

SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_shows ON tv_genres.id = tv_shows.id
WHERE tv_shows.title = 'Dexter';

