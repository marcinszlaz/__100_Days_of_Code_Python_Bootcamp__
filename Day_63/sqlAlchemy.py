from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os

class Library(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Library)
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'new-books-collection.db')
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

class Books(db.Model):
  id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement="auto") #sqlAlchemy take care of autoincrement id column, anyway xD
  title: Mapped[str] = mapped_column(String(250), nullable=False,unique=True)
  author: Mapped[str] = mapped_column(String(250),nullable=False)
  review: Mapped[float] = mapped_column(Float(precision=2), nullable=False)

with app.app_context(): # writing a row, create new record
  db.create_all()
  book = Books(id=None, title="Harry Potter",author="J.K. Rowling", review="9.4")
  db.session.add(book)
  db.session.commit()

with app.app_context(): # update title
  book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
  book_to_update.title = "Harry Potter and the Chamber of Secrets"
  # "Harry Potter and the Chamber of Secrets"
  db.session.commit()

with app.app_context(): # reading rows
  result = db.session.execute(db.select(Books).order_by(Books.title))
  all_books = result.scalars()
  print(all_books.all())

with app.app_context(): # searching book called "Harry Potter..." WHERE clause
  book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter and the Chamber of Secrets")).scalar()
  print(book)

book_id = 1
with app.app_context(): # update query by id
  book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
  # book_to_update = db.get_or_404(Books,book_id) # model class to query and primary key
  book_to_update.title = "Harry Potter and the Goblet of Fire"
  db.session.commit()

book_id = 1
with app.app_context():
  book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
  # book_to_delete = db.session.execute(Books, book_id)
  db.session.delete(book_to_delete)
  db.session.commit()
