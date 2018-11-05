#!/usr/bin/env bash

# TASK - 1
sqlite3 example.db "SELECT title, artist, counter FROM tracks INNER JOIN (SELECT song_id AS _song_id, COUNT(*) AS counter FROM listens GROUP BY song_id ORDER BY COUNT(*) DESC LIMIT 10) ON song_id = _song_id ORDER BY counter DESC;";| sed 's/|/ /g'

# TASK - 2
sqlite3 example.db "SELECT user_id, COUNT(DISTINCT song_id) AS counter FROM listens GROUP BY user_id ORDER BY counter DESC LIMIT 10;";| sed 's/|/ /g'

# TASK - 3
sqlite3 example.db "SELECT artist, COUNT(*) FROM listens AS l INNER JOIN tracks AS t ON l.song_id = t.song_id GROUP BY artist ORDER BY COUNT(*) DESC LIMIT 1;";| sed 's/|/ /g'

# TASK - 4
sqlite3 example.db "SELECT strftime('%m',datetime(date_id, 'unixepoch')) AS months, COUNT(*) FROM listens GROUP BY months ORDER BY months;";| sed 's/|/ /g'

# TASK - 5
sqlite3 example.db "SELECT user_id, COUNT(*) FROM (SELECT DISTINCT user_id, song_id FROM listens WHERE song_id IN (SELECT l_song_id FROM (SELECT song_id AS l_song_id, COUNT(*) AS counter FROM listens GROUP BY song_id) INNER JOIN (SELECT song_id AS q_song_id FROM tracks WHERE UPPER(artist) LIKE 'QUEEN') ON l_song_id = q_song_id ORDER BY counter DESC LIMIT 3)) GROUP BY user_id HAVING COUNT(*) >= 3 ORDER BY user_id LIMIT 10;";| cut -d '|' -f 1