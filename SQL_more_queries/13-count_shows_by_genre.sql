-- This script lists all genres and the count of shows linked to each genre.
-- It filters out genres with no shows and sorts results by the count of shows in descending order.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.tv_show_id) > 0
ORDER BY number_of_shows DESC;
