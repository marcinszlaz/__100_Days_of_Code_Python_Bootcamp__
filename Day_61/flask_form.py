from flask_wtf import FlaskForm
from wtforms import StringField,EmailField, PasswordField,SubmitField
from wtforms.validators import (DataRequired,ValidationError,
                                StopValidation,InputRequired,Email,Length, EqualTo)

class MyForm(FlaskForm):
    email_ = EmailField(label = 'Em@il/Login', validators=[InputRequired(message="type your email"), Email(message="wrong email")])
    password_ = PasswordField(label = 'Password', validators=[InputRequired(message="type your password"),Length(min=8, message="Password is too short"),EqualTo('confirm_',message="passwords doesn't match")])
    confirm_ = PasswordField(label = 'Confirm', validators=[InputRequired(message="retype your password"),Length(min=8, message="Password is too short")])
    submit_ = SubmitField(label = "Log in")
    # you can use built in FlaskForm library(framework?) ready to use templates
    # instead of adding attrs in tags inside html/jinja
    # for eg. {# form.password.label #} {# form.password(size=20,placeholder="myPassword",autocomplete=True, required=True, type="password") #}

    # name = StringField(label = 'name', validators=[DataRequired(message="Mr Anderson, Why!"),InputRequired(message="Type some input")])
    # email = StringField(label = 'email', validators=[DataRequired(message="Mr Anderson, Why!")])
    # password = StringField(label = 'password', validators=[DataRequired(message="Mr Anderson, Why!")])


