-- SELECT * FROM books LIMIT 5 OFFSET 0;
-- SELECT CONCAT_WS('.',SUBSTRING(author_fname,1,1),SUBSTRING(author_lname,1,1),'') as inicjaly FROM books LIMIT 5;
-- SELECT REPLACE('Hello World', 'Hell','%$#@') AS replace_tests;
-- SHOW PROCESSLIST;
-- SELECT REPLACE('milk breed soup eggs',' ',' and ') AS rep;
-- SELECT RPAD(REPLACE((CONCAT_WS(' ',title, author_fname, author_lname)),' ','\\_'),50+(LENGTH(REPLACE(CONCAT_WS(' ',title, author_fname,author_lname),' ','\\_'))/2),'.') AS ciag_znaczkow FROM books;
-- SELECT 50+(LENGTH(REPLACE(CONCAT_WS(' ',title, author_fname,author_lname),' ','\\_'))/2) as ciag FROM books;
-- SELECT RPAD(REPLACE((CONCAT_WS(' ',title, author_fname, author_lname)),' ','\\_'),100,' ') AS ciag_znaczkow FROM books;
-- SELECT book_id AS `numer ksiazki`, RPAD((SUBSTRING(title,1,10)),13,'.') AS `short title 1`, LPAD(SUBSTRING(title,1,10),13,'.') AS `short title 2`, LPAD(RPAD((LEFT(title,10)),13,'.'),16,'.') AS `short title 3`, (CONCAT_WS(', ',author_lname, author_fname)) AS author, CONCAT(stock_quantity,' in stock') AS quantity FROM books;
-- LEFT('text',5) SUBSTRING('text',1,5) robi to samo ale SUBSTRING rowniej sie wyswietla
-- nieprawda, to CONCAT robi tak ze zle sie wyswietla, LEFT I SUBS to samo

-- SELECT user, host, plugin, authentication_string,password_last_changed,password_expired FROM mysql.user WHERE user = 'winuser';
SELECT * FROM mysql.user;