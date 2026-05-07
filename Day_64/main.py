# TODO error with adding existing film to database - take care of it,
# maybe new route with nice info ?
# region Imports
from idlelib.run import flush_stdout

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests, pathlib, os, json
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError
# endregion
# region Maintenance
dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path = dotenv_path)
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
csrf = CSRFProtect(app)
Bootstrap5(app)
# endregion
# region API requests section
def movie_searcher_by_title(params: str = "")->tuple:
  """" function gets str parameter (film name)
       and return tuple with two values
       1)dictionary (json)
       2) same content but nice formatted string          """
  headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Authorization":f"Bearer {os.getenv("BEARER")}"
  }
  parameters = {
    "query":f"{params}"
  }
  response = requests.get(url=os.getenv('API_URL'),headers=headers,params=parameters)
  formatted_dict = json.dumps(response.json(),indent=4,sort_keys=True)
  return response.json(),formatted_dict

def movie_searcher_by_id(movie_id: int)->tuple:
  """ function gets movie_id and returns dictionary
      and formatted str(dictionary) in tuple(dict[0],str[1]) """
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Authorization": f"Bearer {os.getenv("BEARER")}"
  }
  URL = f"{os.getenv('DET_URL')}{movie_id}"
  response = requests.get(url=URL, headers=headers)
  formatted_dict = json.dumps(response.json(), indent=4, sort_keys=True)
  return response.json(), formatted_dict
# endregion
# region Create Database
class Database(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Database)
basedir = os.path.abspath(os.path.dirname(__file__))
DB_URI = 'sqlite:///' + os.path.join(basedir,'movie-project.db')
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db.init_app(app)
# endregion
# region Create Table Movie
class Movie(db.Model):
  id: Mapped[int] = mapped_column(Integer(),primary_key=True,autoincrement=True)
  title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
  year: Mapped[int] = mapped_column(Integer(), nullable=False)
  description: Mapped[str] = mapped_column(String(500),nullable=False)
  rating: Mapped[float] = mapped_column(Float(precision=2), nullable=True)
  ranking: Mapped[int] = mapped_column(Integer(),nullable=True)
  review: Mapped[str] = mapped_column(String(100), nullable=True)
  img_url: Mapped[str] = mapped_column(String(200),nullable=True)
with app.app_context():
  db.create_all()
#  endregion
#region Edit form
class Edit(FlaskForm):
  rating = FloatField(label='Your rating Out of 10 e.g. 7.5',name='rating', validators=[NumberRange(min=1.0,max=10.0,message='digit between 1.0 - 10.0')],render_kw ={"novalidate":False,"autocomplete":False})
  review = StringField(label='Your Review',name='review',render_kw ={"novalidate":False,"autocomplete":False},validators=[DataRequired(message='Type your short opinion')])
  submit = SubmitField(label='Done',name='submit')
# endregion
# region Add form
class Add(FlaskForm):
  title = StringField(label='Movie Title',name='title',validators=[DataRequired(message="Type title of movie which you\'re searching for")])
  submit = SubmitField(label='Add Movie',name='submit')
# endregion
# region Database Feeder
try:
  new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
  )
  second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
  )
  with app.app_context():
    db.session.add(new_movie)
    db.session.add(second_movie)
    # db.session.commit()
except IntegrityError as er:
  print(f'Its ok :) {er}')
# endregion
# region @app.route('/')
@app.route("/",methods=['GET','POST'])
def home():
  with app.app_context():
    # solution with Python list contains rating
    # many requests to database, and here I have to handle with
    # equal rating issue
    # rating_list = db.session.execute(db.select(Movie.rating).order_by(Movie.rating)).scalars().all()
    # print(sorted(rating_list, reverse=True))
    # for rank,rating in enumerate(sorted(rating_list, reverse=True),start=1):
    #   movie_ranking = db.session.execute(db.select(Movie).where(Movie.rating == rating)).scalar()
    #   movie_ranking.ranking = rank
    # solution with list of objects, it is faster, less request to db
    # and it handles with problem equal ratings for few films
    rating_object_list = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
    for rank,object in enumerate(rating_object_list,start=1):
      object.ranking = rank

    my_movies = db.session.execute(db.select(Movie).order_by(Movie.ranking.desc())).scalars().all()
  return render_template("index.html", my_movies=my_movies)
# endregion
# region @app.route('/edit')
@app.route("/edit",methods=['POST','GET'])
def edit():
  form = Edit()
  movie_id = request.args.get('id_')
  change = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
  if form.validate_on_submit():
    change.rating = float(form.data.get('rating'))
    change.review = form.data.get('review')
    db.session.commit()
    return redirect(url_for('home'))
  return render_template('edit.html', form=form,title=change.title)
# endregion
# region @app.route('/delete')
@app.route("/delete",methods=['GET'])
def delete():
  movie_id = request.args.get('movie_id')
  delete_movie = db.get_or_404(Movie,movie_id)
  db.session.delete(delete_movie)
  db.session.commit()
  return redirect(url_for('home'))
# endregion
# region @app.route('/add')
@app.route('/add',methods=['GET','POST'])
def add():
  form = Add()
  if form.validate_on_submit():
    title = form.title.data
    with app.app_context():
      is_movie_exists = db.session.execute(db.select(Movie).where(Movie.title == title)).scalar()
      if is_movie_exists:
        flash(message="This film is exist in your collection!")
        msg = "Wrong!"
        return redirect(url_for('add',msg=msg))
    movie_dict = movie_searcher_by_title(title)
    return render_template('select.html',movie_dict=movie_dict[0]['results'])
  return render_template('add.html',form=form)
# endregion
# region @app.route('/select')
@app.route('/select')
def select():

    return render_template('select.html')
  # endregion
# region @app.route('/seek')
@app.route('/seek')
def seek():
  movie_id = int(request.args.get('id'))
  movie_dict = movie_searcher_by_id(movie_id)
  title = movie_dict[0].get('original_title')
  year = movie_dict[0].get('release_date')[:4]
  img_prefix = os.getenv('IMG_PREF')
  img_url = f"{img_prefix}{movie_dict[0].get('poster_path')}"
  description = movie_dict[0].get('overview')
  movie = Movie(title=title,year=year,img_url=img_url, description=description)
  with app.app_context():
    try:
      db.session.add(movie)
      db.session.commit()
    except IntegrityError as er:
      print('Film is exists in database')
      flash(message="Film is already exists in your database add another one")
      return redirect(url_for('add'))
    else:
      id_ = db.session.execute(db.select(Movie.id).where(Movie.title == title)).scalar()
      return redirect(url_for('edit',id_ = id_))
# endregion
# region Name Check
if __name__ == '__main__':
  app.run(debug=True, host=os.getenv("HOST_IP"), port=os.getenv("HOST_PORT"))
#endregion

