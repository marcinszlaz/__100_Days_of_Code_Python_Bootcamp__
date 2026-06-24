from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Event
from forms import LoginForm, RegisterForm, EventForm
from utils import send_email
from datetime import datetime
import calendar

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@login_required
def index():
    return redirect(url_for("calendar_view"))


@app.route("/calendar")
@login_required
def calendar_view():
    year = datetime.now().year
    month = datetime.now().month

    cal = calendar.monthcalendar(year, month)
    events = Event.query.filter_by(user_id=current_user.id).all()

    return render_template("calendar.html", cal=cal, month=month, year=year, events=events)


@app.route("/add_event", methods=["GET", "POST"])
@login_required
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            date=form.date.data,
            user_id=current_user.id
        )
        db.session.add(event)
        db.session.commit()

        flash("Event zapisany")
        return redirect(url_for("calendar_view"))

    return render_template("add_event.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("calendar_view"))
        else:
            flash("Błędne dane logowania")

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        send_email(user.email, "Witaj!", "Dziękujemy za rejestrację")

        flash("Konto utworzone")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
