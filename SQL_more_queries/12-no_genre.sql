-- The script lists shows contained in database
SELECT m.title "title", sg.genre_id "genre_id"
FROM tv_shows m
LEFT JOIN tv_show_genres sg
	ON sg.show_id = m.id
	WHERE sg.show_id IS NULL
ORDER BY m.title;
