#!/usr/bin/env bash

sqlite3 example.db << EOF

CREATE TABLE listens_temp(
  user_id varchar(18) NOT NULL,
  song_id varchar(18) NOT NULL,
  date_id varchar(12) NOT NULL
);
CREATE TABLE listens (
  id integer primary key,
  user_id varchar(18) NOT NULL,
  song_id varchar(18) NOT NULL,
  date_id varchar(12) NOT NULL,
  FOREIGN KEY (song_id) REFERENCES tracks(song_id)
);
CREATE INDEX listens_song_id_index ON listens (song_id);

CREATE TABLE tracks_temp (
  track_id varchar2(18) NOT NULL,
  song_id varchar2(18) NOT NULL,
  artist varchar2(256) DEFAULT NULL,
  title varchar2(256) DEFAULT NULL
  );
CREATE TABLE tracks (
  song_id varchar2(18) NOT NULL,
  artist varchar2(256) DEFAULT NULL,
  title varchar2(256) DEFAULT NULL
  );
CREATE INDEX tracks_artist_index ON tracks (artist);

.mode csv
.separator ,
.import unique_tracks.txt tracks_temp
.mode column

insert into tracks(song_id, artist, title) select song_id,artist,title from tracks_temp;
drop table tracks_temp;

.mode csv
.separator ,
.import triplets_sample_20p.txt listens_temp
.mode column

insert into listens(user_id, song_id, date_id) select * from listens_temp;
drop table listens_temp;