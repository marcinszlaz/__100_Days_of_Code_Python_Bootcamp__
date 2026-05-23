from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, URLField,PasswordField
from wtforms.validators import DataRequired, URL, Email, EqualTo
from flask_ckeditor import CKEditorField

# region WTForm for creating a blog post
class CreatePostForm(FlaskForm):
  title = StringField("Blog Post Title", validators=[DataRequired()])
  subtitle = StringField("Subtitle", validators=[DataRequired()])
  img_url = StringField("Blog Image URL", validators=[DataRequired()])
  body = CKEditorField("Blog Content", validators=[DataRequired()])
  submit = SubmitField("Submit Post")
# endregion

# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
  name = StringField("Type your username", validators=[DataRequired()])
  email = EmailField(label = "Type your user email", validators=[Email(),DataRequired()])
  password = PasswordField("Type your password", validators=[DataRequired()])
  password2 = PasswordField("Retype your user password", validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField("Send Data")

# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
  email = EmailField(label="Type your user email", validators=[DataRequired(), Email()])
  password = PasswordField("Type your password", validators=[DataRequired()])
  submit = SubmitField("Log in")

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
  body = CKEditorField("Comment", validators=[DataRequired()])
  submit = SubmitField("Send comment")
