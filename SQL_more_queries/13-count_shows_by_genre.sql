-- The script lists genres from the database and displays the number of shows linked.
SELECT g.name "genre", COUNT(sg.genre_id) "number_of_shows" 
FROM tv_genres g
JOIN tv_show_genres sg
	ON g.id = sg.genre_id
GROUP BY sg.genre_id
ORDER BY COUNT(sg.genre_id)  DESC;
