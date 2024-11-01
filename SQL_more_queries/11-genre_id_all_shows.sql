-- This script lists all shows and their genre IDs
-- from the 'tv_shows' and 'tv_show_genres' tables in the 'hbtn_0d_tvshows' database.
-- If a show does not have a genre, it will display NULL.
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
