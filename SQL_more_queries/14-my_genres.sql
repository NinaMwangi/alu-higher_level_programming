-- This script lists all genres in the database
SELECT g.name
FROM tv_shows m
JOIN tv_show_genres sg
	ON sg.show_id = m.id
JOIN tv_genres g
	ON sg.genre_id = g.id
WHERE m.title = 'Dexter'
ORDER BY g.name;
