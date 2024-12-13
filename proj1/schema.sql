-- drop table if exists posts;

-- create table posts(
--   id integer primary key autoincrement,
--   created timestamp not null  default current_timestamp,
--   title text not null,
--   content text not null
-- );

-- drop table if exists info;

-- create table info(
--   peru text not null,
--   phone integer primary key,
--   addr text not null
-- );

drop table if exists login_table;

CREATE TABLE login_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    passw TEXT NOT NULL,
    email TEXT NOT NULL
);