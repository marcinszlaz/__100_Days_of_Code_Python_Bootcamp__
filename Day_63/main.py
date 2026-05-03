from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect # it works independently apart flask.wtf forms
from dotenv import load_dotenv
import os, pathlib
from flask_bootstrap import Bootstrap5 as bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, create_engine
from sqlalchemy.exc import IntegrityError
import pandas as pd
import sqlite3

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path = dotenv_path)

app = Flask(__name__)

# database part
class Library(DeclarativeBase): # basically we crate here class aka database
  pass

db = SQLAlchemy(model_class=Library) # and here we're wrapping around this base from sqlalchemy using flask-sqlalchemy wrapper
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'new-books-collection.db')
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

class Books(db.Model): # here we're creating table `books` inside database
  id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement="auto") #sqlAlchemy take care of autoincrement id column, anyway xD
  title: Mapped[str] = mapped_column(String(250), nullable=False,unique=True)
  author: Mapped[str] = mapped_column(String(250),nullable=False)
  review: Mapped[float] = mapped_column(Float(precision=2), nullable=False)



app.config['SECRET_KEY'] = 'my-super-secret-key'
csrf = CSRFProtect(app)
bootstrap = bootstrap5(app)
all_books = []
show_books = None

@app.route('/', methods=["GET","POST"])
def home():
  global all_books
  if request.method == 'GET' or 'POST':
    with app.app_context():
      show_books = db.session.execute(db.select(Books.title, Books.author, Books.review)).tuples().all()
  try:
    if request.method == 'POST':
      all_books.append({k: v for k, v in request.form.items() if k != 'csrf_token'})
      print('all_books list: ',all_books)
      title = request.form['title']
      author = request.form['author']
      review = request.form['rating']
      print('t,a,r: ',title,author,review)
      with app.app_context():  # writing a row, create new record
        db.create_all()
        # try:
        books_ = Books(id=None, title=title, author=author, review=review)
        db.session.add(books_)
        db.session.commit()
        # except Exception as er:
        #   print(f"Book probably exists in database {er}")
      with app.app_context():
        show_books = db.session.execute(db.select(Books.title, Books.author, Books.review)).tuples().all()
        print(show_books) # list of tuples
        # conn = sqlite3.connect('new-books-collection.db')
        # engine = create_engine('sqlite:///new-books-collection.db')
        # df = pd.read_sql_query("SELECT * FROM books",engine)
        # print(df)
  except (IntegrityError, Exception) as er:
    print(f'We got an error {er}')
  return render_template('index.html', all_books=all_books,show_books=show_books)

@app.route("/add",methods=["POST","GET"])
def add():
    global all_books
    try:
      if request.method == 'POST':
        all_books.append({k: v for k, v in request.form.items() if k != 'csrf_token'})
    except (IntegrityError, Exception) as er:
      print(f'We got an error {er}')
    return render_template('add.html',all_books=all_books)

if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("HOST_IP"), port=os.getenv("HOST_PORT"))

# all_books.extend([{k:v for k,v in request.form.items()}]) extend() and += are qual in action
# all_books+=([{k:v for k,v in request.form.items()}])
# all_books.append([{k:v for k,v in request.form.items()}])
# all_books.append([{k:v} for k,v in request.form.items()])
# all_books.append(request.form.to_dict()) # this is the most clear way