from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.exc import IntegrityError
import os,pathlib
from dotenv import load_dotenv

path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path = path)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('KEY')
app.config['UPLOAD_FOLDER'] = './static/files'

# CREATE LOGIN SYSTEM
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
  return db.get_or_404(User,user_id)

# CREATE DATABASE
class Base(DeclarativeBase):
  pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin,db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  email: Mapped[str] = mapped_column(String(100), unique=True)
  password: Mapped[str] = mapped_column(String(100))
  name: Mapped[str] = mapped_column(String(1000))
with app.app_context():
  db.create_all()

@app.route('/')
@app.route('/index')
def home():
  user = User()
  logged_in = current_user
  return render_template("index.html", logged_in = logged_in)

@app.route('/register',methods=['GET','POST'])
def register():
  if request.method == 'POST':
    gph = generate_password_hash
    fd = request.form.to_dict() # form_dict
    dwh = {k:(v if k!='password' else gph(password=v,method="pbkdf2:sha256:100000",salt_length=8))
           for k,v in fd.items()} # dict with pbkdf2 hashed password
    is_email_exist = db.session.execute(db.select(User).where(User.email==dwh['email'])).scalar()
    if is_email_exist:
      flash('You have already registered!')
      return redirect('login')
    else:
      new_user = User(**dwh)
      db.session.add(new_user)
      db.session.commit()
      # return redirect(url_for('secrets',name=name)) # here you take name in url it requires {{ request.args.get('name') }} in html code
      return redirect ('login')
  return render_template("register.html",logged_in=current_user)

@app.route('/login', methods=['POST','GET'])
def login():
  error = None
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = db.session.execute(db.select(User).where(User.email==email)).scalar()
    if not user:
      flash('User not found')
    elif not check_password_hash(user.password, password):
      flash('Invalid Password')
    else:
      login_user(user)
      flash(f'You were successfully logged in {user.name}')
      return render_template('secrets.html',name=user.name)
  return render_template(template_name_or_list = "login.html", error=error, logged_in=current_user)

@app.route('/secrets')
@login_required
def secrets():
  return render_template("secrets.html")

@app.route('/logout')
# @login_required
def logout():
  logout_user()
  return render_template('index.html')

@app.route('/download')
@login_required
def download():
  return send_from_directory(app.config['UPLOAD_FOLDER'],'cheat_sheet.pdf',as_attachment=False)

if __name__ == "__main__":
  app.run(debug=True,host=os.getenv('HOST_IP'))
