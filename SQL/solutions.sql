 -- rozwiazania problemow z kurs

-- ********* FINDING 5 OLDEST USERS ******************** 
SELECT * FROM users ORDER BY created_at ASC LIMIT 5;

-- ********* MOST POPULAR REGISTRATION DAY *************
-- sposob pierwszy z zwyklym order by
SELECT
COUNT(DAYOFWEEK(created_at)) AS day_count,
DATE_FORMAT(created_at,'%W') AS day_name
FROM users
GROUP BY day_name ORDER BY day_count DESC;

-- sposob drugi z funkcja window, przeglad wszystkich row
-- bez wyszczegolnienia interesujacych nas wynikow
SELECT
username,
DATE(created_at) AS date,
COUNT(DAYOFWEEK(created_at)) OVER(PARTITION BY DAYOFWEEK(created_at)) AS day_num,
DATE_FORMAT(created_at,'%W') AS day_name
FROM users LIMIT 10;

-- znowu z window ale z uzyciem slowa kluczowego distinct
-- to slowo musi byc uzywane ostroznie, jako prefix moze byc uzyte
-- chyba tylko w 1 szej kolumnie
SELECT
DISTINCT COUNT(DAYOFWEEK(created_at)) OVER(PARTITION BY DAYOFWEEK(created_at)) AS day_num,
DATE_FORMAT(created_at,'%W') AS day_name
FROM users
ORDER BY day_num DESC;

-- rowniez window i distinct
SELECT
DISTINCT DATE_FORMAT(created_at, '%W') AS day_name,
COUNT(*) OVER(PARTITION BY  DAYOFWEEK(created_at)) AS day_num
FROM users
ORDER BY day_num DESC;

/* ************* FIND THE USERS WHO HAVE NEVER POSTED A PHOTO */
-- solution 1
SELECT
ROW_NUMBER() OVER(ORDER BY username) AS numerki,
username,
IFNULL(image_url,'brak postow') AS posty
FROM users
LEFT JOIN photos ON users.id = photos.user_id
WHERE image_url IS NULL LIMIT 10 OFFSET 20;

-- solution 2 :)
SELECT 
ROW_NUMBER() OVER(ORDER BY username) AS nr,
username,
COUNT(image_url) AS img_count
FROM users LEFT JOIN photos ON users.id=photos.user_id
GROUP BY username HAVING(img_count=0) LIMIT 10;

-- solution 3 :)
SELECT ROW_NUMBER() OVER(ORDER BY username) AS nr, username, image_url, SUM(IFNULL(image_url,1)) OVER() AS bad_users FROM (SELECT username, image_url FROM users LEFT JOIN photos ON users.id = photos.user_id WHERE photos.id IS NULL) as kwer LIMIT 10;

-- WHO HAVE THE HIGHEST NUMBER OF LIKES AT THEY PHOTO !
-- solution 1
SELECT username, photo_id, image_url, COUNT(likes.user_id) AS like_count FROM likes JOIN photos ON likes.photo_id=photos.id  JOIN users ON users.id=photos.user_id GROUP
BY photo_id ORDER BY like_count DESC LIMIT 10;

-- HOW MANY TIMES DOES THE AVERAGE USER POST ?
-- solution 1
SELECT COUNT(users.id) AS users_count, (SELECT COUNT(photos.id) FROM photos) AS posts_count, ROUND(((SELECT COUNT(photos.id) FROM photos)/(SELECT COUNT(users.id) FROM users)),2) AS average_posts_per_user  FROM users;

-- to wymyslil czacik xD
SELECT AVG(post_count) FROM (
    SELECT users.id, CO
    -- to wymyslil czacik xDUNT(photos.id) AS post_count
    FROM users
    LEFT JOIN photos ON users.id = photos.user_id
    GROUP BY users.id
) AS user_activity;

-- WHAT ARE THE TOP 5 MOST COMMONLY USED HASTAGS ---
-- solution 1
-- join tabeli photos jest niekonieczny ale ładny
SELECT tag_name, COUNT(photo_id) AS tag_count FROM tags JOIN photo_tags ON tags.id=photo_tags.tag_id LEFT JOIN photos ON photo_tags.photo_id=photos.id   GROUP BY tag_name ORDER BY tag_count DESC  LIMIT 5

-- FIND USERS WHO HAVE LIKED EVERY SINGLE PHOTO --
-- szukamy botow xD
/* trzeba zalozyc, ze boot ktory polubia wszystkie
   zdjecia polubie `wszystkie zdjecia` w bazie lub
   wiecej, po 1+ lajku na fotke */

-- rozwiazanie 1, troche niezgrabne, okazuje sie ze bardzo zgrabne
-- to co tu jest zrobione strukturalnie, wykonuje klauzula HAVING 
SELECT data.pi,username FROM (SELECT username, COUNT(photo_id) AS pi FROM users LEFT JOIN likes ON users.id=likes.user_id GROUP BY username) AS data WHERE data.pi >= (SELECT COUNT(*) FROM photos);

-- inne rozwiazanie
SELECT username, COUNT(photo_id) AS count FROM users JOIN likes ON users.id=likes.user_id GROUP BY username HAVING count >= (SELECT COUNT(*) FROM photos);

















