from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os, pathlib
from flask_bootstrap import Bootstrap5 as bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy.exc import IntegrityError

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path = dotenv_path)

app = Flask(__name__)

# database part
class Library(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Library)
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'new-books-collection.db')
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

class Books(db.Model):
  id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement="auto")
  title: Mapped[str] = mapped_column(String(250), nullable=False,unique=True)
  author: Mapped[str] = mapped_column(String(250),nullable=False)
  review: Mapped[float] = mapped_column(Float(precision=2), nullable=False)

app.config['SECRET_KEY'] = 'my-super-secret-key'
csrf = CSRFProtect(app)
bootstrap = bootstrap5(app)
show_books = None

@app.route('/', methods=["GET","POST"])
def home():
  show_books = db.session.execute(db.select(Books.id,Books.title,Books.author,Books.review)).tuples().all()
  return render_template('index.html', show_books=show_books)

@app.route("/add",methods=["POST","GET"])
def add():
    if request.method == 'GET':
      return render_template('add.html')
    if request.method =='POST':
      title = request.form.get('title')
      author = request.form.get('author')
      review = request.form.get('review')
      with app.app_context():
        new_row = Books(title=title,author=author,review=review)
        db.session.add(new_row)
        db.session.commit()
      return redirect(url_for('home'))

@app.route('/edit', methods=['GET','POST'])
def edit():
  if request.method == 'GET':
    book_id = request.args.get('id_')
    with app.app_context():
      title_and_review = db.session.execute(db.select(Books.title,Books.review,Books.id).where(Books.id == book_id)).tuples().all()
    return render_template(template_name_or_list = 'edit.html',title_and_review=title_and_review)
  if request.method == 'POST':
    id_book_to_change = request.form.get('b_id')
    new_rating = request.form.get('rating-update')
    change_rating = db.get_or_404(Books,id_book_to_change)
    change_rating.review = float(new_rating)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete')
def delete():
  id_book_to_delete = request.args.get('buuk_ajdi')
  book_to_delete_ = db.session.execute(db.select(Books).where(Books.id == id_book_to_delete)).scalar()
  book_to_delete = db.get_or_404(Books, id_book_to_delete)
  print(book_to_delete_, book_to_delete)
  db.session.delete(book_to_delete)
  db.session.commit()

  return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("HOST_IP"), port=os.getenv("HOST_PORT"))

