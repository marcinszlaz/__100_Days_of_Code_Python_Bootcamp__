/* skrypt tworzony na potrzeby cwiczenia z udemy, kurs coolt steele
czy jakos tak, skrypt uruchomimy w mysql \. skrypt.sql albo source ./skrypt.sql
*/


DROP DATABASE IF EXISTS insta_db;
CREATE DATABASE IF NOT EXISTS insta_db;

USE insta_db;

CREATE TABLE users (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) COMMENT='uzytkownicy insta';

CREATE TABLE photos(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    image_url VARCHAR(255) NOT NULL,
    user_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY `users\_photos` (user_id) REFERENCES users(id)
) COMMENT='komentarz taktyczny xd';

CREATE TABLE comments(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    comment_text VARCHAR(255) NOT NULL,
    user_id INTEGER NOT NULL,
    photo_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY `users\_comments` (user_id) REFERENCES users(id),
    FOREIGN KEY `photos\_comments` (photo_id) REFERENCES photos(id)
) COMMENT='na siedem znakow';

-- tabela z like'ami wydaje sie ciekawa, nietypowy priamry key
CREATE TABLE likes(
    user_id INTEGER NOT NULL,
    photo_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY `users\_likes` (user_id) REFERENCES users(id),
    FOREIGN KEY `photos\_likes` (photo_id) REFERENCES photos(id),
    PRIMARY KEY(user_id, photo_id)
) COMMENT='primary key is combination of two foreign keys';

-- ta kombinacja pk / 2fk wynika z tego, ze mozna obserwowac
-- kogos a ten ktos moze obserwowac ciebie follower / followee
-- ale nie mozna obserwowac kogos 2 razy, czyli jedno id usera
-- moze ogladac inne id usera ale nie moze byc 2-3 i wiecej
-- razy jedno id patrzaca na inne, to takie wymuszenie unique
CREATE TABLE follows(
    follower_id INTEGER NOT NULL,
    followee_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY `users\_follows` (follower_id) REFERENCES users(id),
    FOREIGN KEY `users\_follows1` (followee_id) REFERENCES users(id),
    PRIMARY KEY(follower_id,followee_id)
) COMMENT='tutaj podobnie, pk zlozony z 2 fk';

CREATE TABLE tags(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    tag_name VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE photo_tags(
    photo_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY `photos\_photo_tags` (photo_id) REFERENCES photos(id),
    FOREIGN KEY `tags\_photo_tags` (tag_id) REFERENCES tags(id),
    PRIMARY KEY(photo_id, tag_id)
);

