import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

db = sqlite3.connect(database="books-collection.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS  books (id INTEGER  PRIMARY KEY AUTOINCREMENT, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute('INSERT INTO books(title,author,rating) values("1984","George Orwell","7.6"),("1985","George Orwell","7.6"),("1986","George Orwell","7.6")')

db.commit()

show = cursor.execute("SELECT * FROM books")
print(show.fetchall())