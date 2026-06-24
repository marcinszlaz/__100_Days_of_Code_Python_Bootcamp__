from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(message = 'Pole jest wymagane, wprowadź nazwę użytkownika')])
    password = PasswordField('Hasło', validators=[DataRequired(message = 'Pole jest wymagane, wprowadź hasło')])
    remember_me = BooleanField('Zapamiętaj mnie')
    submit = SubmitField('Zaloguj Się')

