1. Technologie
- sqlite - pozwala na łatwe wykonywanie zapytań i stosunkowo dobrą efeketwyność zapytań sql, przydatne przy tworzeniu baz o małym stopniu skomplikowania.
- bash - pozwala na szybką obróbkę tekstu, dobrze współpracuje z sqlite

2. Schemat
TABLE tracks
  song_id varchar2(18) NOT NULL,
  artist varchar2(256) DEFAULT NULL,
  title varchar2(256) DEFAULT NULL

TABLE listens
  id integer primary key,
  user_id varchar(18) NOT NULL,
  song_id varchar(18) NOT NULL,
  date_id varchar(12) NOT NULL,
  FOREIGN KEY (song_id) REFERENCES tracks(song_id)