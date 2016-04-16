drop table if exists queue; 
drop table if exists parties;
create table songs (
  songid integer primary key autoincrement, 
  song text not null, 
  votes integer not null,
  users text not null
);
create table parties (
  id integer primary key autoincrement,
  party text not null,
  password text not null, 
  songid integer,
  foreign key(songid) references songs(songid)
);