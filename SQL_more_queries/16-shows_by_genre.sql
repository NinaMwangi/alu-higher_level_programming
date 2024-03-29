-- Lists all shows and all genres linked to that show.
SELECT m.title, g.name
FROM tv_shows m
LEFT OUTER JOIN tv_show_genres sg
	ON sg.show_id = m.id
LEFT OUTER JOIN tv_genres g
	ON sg.genre_id = g.id
ORDER BY m.title, g.name;
