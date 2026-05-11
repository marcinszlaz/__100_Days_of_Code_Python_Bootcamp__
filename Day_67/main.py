
# region--import_region--
from flask import Flask, render_template, redirect, url_for,request, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from flask_ckeditor.utils import cleanify
from datetime import date
import os, pathlib, json
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError
# endregion
# region --maintenance--
dotenv_path = pathlib.Path.cwd() / '.env'
load_dotenv(dotenv_path = dotenv_path)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET')
Bootstrap5(app)
ckeditor = CKEditor(app)
# endregion
# region --CREATE DATABASE--
class Base(DeclarativeBase):
  pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
# endregion
# region --CONFIGURE TABLE--
class BlogPost(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
  subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
  date: Mapped[str] = mapped_column(String(), default= lambda: date.today().strftime('%B %d, %Y'), nullable=False)
  body: Mapped[str] = mapped_column(Text, nullable=False)
  author: Mapped[str] = mapped_column(String(250), nullable=False)
  img_url: Mapped[str] = mapped_column(String(250), nullable=False)
  def make_dictionary(self):
    dict_ = {column.name: getattr(self, column.name) for column in self.__table__.columns}
    print(json.dumps(dict_, indent=2, sort_keys=True))
    return dict_
with app.app_context():
  db.create_all()
# endregion
# region --Blog_Form--
class MyBlogForm(FlaskForm):
  title = StringField('The blog post title', validators=[DataRequired()])
  subtitle = StringField('The subtitle', validators=[DataRequired()])
  author = StringField('The author\'s name', validators=[DataRequired()])
  img_url = StringField('A URL for the background image', validators=[DataRequired()])
  body = CKEditorField('The body (the main content) of the post', validators=[DataRequired()])
  submit = SubmitField(label='SUBMIT POST')
# endregion
# region--get_all_posts--
@app.route('/')
def get_all_posts():
  # TODO: Query the database for all the posts. Convert the data to a python list.
  posts = db.session.execute(db.select(BlogPost)).scalars().all()
  year = date.today().year
  return render_template("index.html", all_posts=posts, date=date, year=year)
# endregion
# region--show_individual_post--
# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
  # TODO: Retrieve a BlogPost from the database based on the post_id
  requested_post = db.get_or_404(BlogPost,post_id)
  return render_template("post.html", post=requested_post, date=date)
# endregion
# region--new-post--
# TODO: add_new_post() to create a new blog post
@app.route('/add-new-post', methods=['GET','POST'])
def add_new_post():
  form = MyBlogForm()
  please_ignore = ('csrf_token','submit')
  if form.validate_on_submit():
    data_dict = {k:cleanify(v) for k,v in request.form.to_dict().items() if k not in please_ignore}
    new_row = BlogPost(**data_dict)
    with app.app_context():
      try:
        db.session.add(new_row)
        db.session.commit()
      except IntegrityError as er:
        # TODO create own validator instead of this json respond
        msg = {"INFO": {"header": "--Database Integrity Error--","title": f"title {data_dict.get('title')} is occupied",
                        "error":f"{er}"}}
        return jsonify(ERROR=msg), 404
      except Exception as er:
        return jsonify(ERROR=f"--Database Error {er}"),403
      else:
        return redirect(url_for('get_all_posts'))
  return render_template('make-post.html',form=form)
# endregion
# region--edit-post--
# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=['GET','POST'])
def edit_post(post_id):
  # post = db.get_or_404(BlogPost, post_id) # LONGER, LESS FANCY CODE
  # edit_form = CreatePostForm(
  #   title=post.title,
  #   subtitle=post.subtitle,
  #   img_url=post.img_url,
  #   author=post.author,
  #   body=post.body
  # )
  # if edit_form.validate_on_submit():
  #   post.title = edit_form.title.data
  #   post.subtitle = edit_form.subtitle.data
  #   post.img_url = edit_form.img_url.data
  #   post.author = edit_form.author.data
  #   post.body = edit_form.body.data
  #   db.session.commit()
  post = db.get_or_404(BlogPost,post_id) # fetching record from db
  form = MyBlogForm(obj=post) # populate wtf flask form by db object content
  if form.validate_on_submit(): # after post and form fields validation
    form.populate_obj(post) # populate reference to object from db by modified content of wtf flask form
    db.session.add(post) # add modified object to database
    db.session.commit() # commit changes
    return redirect(url_for('show_post',post_id = post_id))
  return render_template('make-post.html', form=form, edit_flag=post_id, date=date)
# endregion
# region--delete-post--
# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>')
def delete(post_id):
  delete_post = db.get_or_404(BlogPost,post_id)
  db.session.delete(delete_post)
  db.session.commit()
  return redirect(url_for('get_all_posts'))
# endregion
# Below is the code from previous lessons. No changes needed.
# region--about--
@app.route("/about")
def about():
  return render_template("about.html",date=date)
# endregion
# region--contact--
@app.route("/contact")
def contact():
  return render_template("contact.html", date=date)
# endregion
# region--name_checking--
if __name__ == "__main__":
  app.run(debug=True, port=os.getenv('HOST_PORT'), host=os.getenv('HOST_IP'))
# endregion
