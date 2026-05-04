from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, pathlib, os
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError

dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path = dotenv_path)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
csrf = CSRFProtect(app)
Bootstrap5(app)

# CREATE DB
class Database(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Database)
basedir = os.path.abspath(os.path.dirname(__file__))
DB_URI = 'sqlite:///' + os.path.join(basedir,'movie-project.db')
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer(),primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer(), nullable=False)
    description: Mapped[str] = mapped_column(String(500),nullable=False)
    rating: Mapped[float] = mapped_column(Float(precision=2), nullable=False)
    ranking: Mapped[int] = mapped_column(Integer())
    review: Mapped[str] = mapped_column(String(100))
    img_url: Mapped[str] = mapped_column(String(200))

with app.app_context():
    db.create_all()

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
        db.session.commit()
except IntegrityError as er:
    print('Its ok :)')

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv("HOST_IP"), port=os.getenv("HOST_PORT"))
