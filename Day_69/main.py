# region import
import hashlib
from urllib.parse import urlencode
from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import sys
import bleach
from tags import allowed_post_tags, allowed_post_attrs
# endregion
# region maintenance
print('we using: ',sys.executable) # we've had problems with dependencies, that's why
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)
# endregion
# region gravatar
gravatar = Gravatar(app)
# endregion
# region Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
  return db.get_or_404(User,user_id)
# endregion
# region OLD DATABASE
# class Base(DeclarativeBase):
#   pass
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
# db = SQLAlchemy(model_class=Base)
# db.init_app(app)
# endregion
# region OLD TABLES
# class BlogPost(db.Model):
#   __tablename__ = "blog_posts"
#   id: Mapped[int] = mapped_column(Integer, primary_key=True) # autoincrement pk by default
#   title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
#   subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
#   date: Mapped[str] = mapped_column(String(250), nullable=False)
#   body: Mapped[str] = mapped_column(Text, nullable=False)
#   author: Mapped[str] = mapped_column(String(250), nullable=False)
#   img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# class User(UserMixin,db.Model):
#   __tablename__ = "user_table"
#   id: Mapped[int] = mapped_column(Integer, primary_key=True) #autoincrement pk by default
#   name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
#   email: Mapped[str] = mapped_column(String(50), nullable=False)
#   password: Mapped[str] = mapped_column(String(100), nullable=False)
# with app.app_context():
#   db.create_all()
# endregion
# region NEW DATABASE
class Base(DeclarativeBase):
  pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
# endregion
# region NEW TABLES
class User(UserMixin,db.Model):
  __tablename__ = "user_table"
  id: Mapped[int] = mapped_column(Integer, primary_key=True) #autoincrement pk by default
  name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  email: Mapped[str] = mapped_column(String(50), nullable=False)
  password: Mapped[str] = mapped_column(String(100), nullable=False)
  posts: Mapped[list["BlogPost"]] = relationship(back_populates = "author")
  comments: Mapped[list["Comment"]] = relationship(back_populates="author")

class BlogPost(db.Model):
  __tablename__ = "blog_posts"
  id: Mapped[int] = mapped_column(Integer, primary_key=True) # autoincrement pk by default
  title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
  subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
  date: Mapped[str] = mapped_column(String(250), nullable=False)
  body: Mapped[str] = mapped_column(Text, nullable=False)
  # author: Mapped[str] = mapped_column(String(250), nullable=True)
  img_url: Mapped[str] = mapped_column(String(250), nullable=False)
  author_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
  author: Mapped["User"] = relationship(back_populates ="posts")
  comments: Mapped[list["Comment"]] = relationship(back_populates="parent_post")

class Comment(db.Model):
  __tablename__ = "comments"
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  text: Mapped[str] = mapped_column(String(500), nullable=True)
  author_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
  author: Mapped["User"] = relationship(back_populates="comments")
  post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"))
  parent_post: Mapped["BlogPost"] = relationship(back_populates="comments")

with app.app_context():
  db.create_all()
# endregion
# region customized decorators
# honestly, I completely don't know why this decorator work, but it's work xD
def admin_only(f): # decorator(function) take function as a/an par/arg
  @wraps(f) # you take as arg view function, @wraps guarantees your view function don't lose its original name (without @wraps for eg. `login` will be renamed by wrapper and whole app will crash)
  def wrapper(*args, **kwargs): # decorator takes only one `f` parameter/argument but wrapper func doesn't know how many pars/agrs `f` will take, that's why *a,**k
    if current_user.id != 1: # if user hasn't id equal 1 return error, otherwise return wrapped view function
      return abort(code=403)
    return f(*args,**kwargs)
  return wrapper # you can't return none, you have return something (reference to wrapper func)
# endregion
# region register
@app.route('/register', methods=['POST','GET'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    email = form.data.get('email')
    name = form.data.get('name')
    password = form.data.get('password')
    hash_hash = generate_password_hash(password=password,method='pbkdf2:sha256',salt_length=8)
    new_user = User(name = name, email = email, password = hash_hash)
    check_email = db.session.execute(db.select(User).where(User.email==email)).scalar()
    if check_email:
      flash('You\'re already signed in with this email')
      return redirect(url_for('login'))
    else:
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user) # login fresh registered user
      return redirect(url_for('get_all_posts'))
  return render_template(template_name_or_list = 'register.html', form=form, date=date)
# endregion
# region login
@app.route('/login',methods=['POST','GET'])
def login():
  form = LoginForm()
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = db.session.execute(db.select(User).where(User.email==email)).scalar()
    if not user:
      flash('User not found, try again')
    elif not check_password_hash(user.password, password):
      flash('Invalid password, try again')
    else:
      login_user(user)
      # flash(f'You were successfully logged in {user.name}')
      return redirect(url_for('get_all_posts'))
  return render_template(template_name_or_list = "login.html",form=form, date=date)
# endregion
# region logout
@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('get_all_posts'))
# endregion
# region main route
@app.route('/')
def get_all_posts():
  result = db.session.execute(db.select(BlogPost))
  posts = result.scalars().all()
  return render_template(template_name_or_list="index.html", all_posts=posts, current_user=current_user, date=date)
# endregion
# region post
# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=['GET','POST'])
# @login_required
def show_post(post_id):
  form = CommentForm()
  requested_post = db.get_or_404(BlogPost, post_id)
  user_obj = db.get_or_404(User,current_user.id)
  comments = db.session.execute(db.select(Comment).where(Comment.post_id==post_id)).scalars().all()
  if form.validate_on_submit():
    if current_user.is_authenticated:
      dirty_text = form.data.get('body') # bleach will bleach'em all malicious content inside HTML code (in theory xD)
      clean_text = bleach.clean(dirty_text,tags = allowed_post_tags, strip=True) # with bleach you can safely use |safe filter inside HTML code
      post_id = requested_post.id
      new_row = Comment(text = clean_text,post_id = post_id,author=user_obj) # you don't have to put inside direct values from
      # other tables, you can use WHOLE table OBJECT or even constructor alone! as kwarg = value(), HAHAHA, nope xD
      # IntegrityError with constructor xD, it have to be object from db table, selected by id or something like this
      db.session.add(new_row)
      db.session.commit()
      comments = db.session.execute(db.select(Comment).where(Comment.post_id==post_id)).scalars().all()
      return render_template("post.html", post=requested_post, date=date, form=form, comments=comments,gravatar=gravatar)
    else:
      return redirect(url_for('login'))
  return render_template("post.html", post=requested_post, date=date, form=form, comments=comments,gravatar=gravatar)
# endregion
# region new_post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
  form = CreatePostForm()
  if form.validate_on_submit():
    new_post = BlogPost(
      title=form.title.data,
      subtitle=form.subtitle.data,
      body=(bleach.clean(form.body.data,tags=allowed_post_tags,strip=True)),
      img_url=form.img_url.data,
      author=current_user,
      date=date.today().strftime("%B %d, %Y")
    )
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))
  return render_template("make-post.html", form=form, date=date)
# endregion
# region edit_post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
  post = db.get_or_404(BlogPost, post_id)
  edit_form = CreatePostForm(
    title=post.title,
    subtitle=post.subtitle,
    img_url=post.img_url,
    author=post.author,
    body=post.body
  )
  if edit_form.validate_on_submit():
    post.title = edit_form.title.data
    post.subtitle = edit_form.subtitle.data
    post.img_url = edit_form.img_url.data
    post.author = current_user
    post.body = bleach.clean(edit_form.body.data,tags=allowed_post_tags,strip=True)
    db.session.commit()
    return redirect(url_for("show_post", post_id=post.id))
  return render_template("make-post.html", form=edit_form, is_edit=True, date=date)
# endregion
# region delete
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
  post_to_delete = db.get_or_404(BlogPost, post_id)
  db.session.delete(post_to_delete)
  db.session.commit()
  return redirect(url_for('get_all_posts'))
# endregion
# region about
@app.route("/about")
def about():
  return render_template(template_name_or_list = "about.html", date=date)
# endregion
# region contact
@app.route("/contact")
def contact():
  return render_template("contact.html", date=date)
# endregion
# region nameCheck
if __name__ == "__main__":
  app.run(debug=True, port=5001, host="0.0.0.0")
# endregion