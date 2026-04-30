from flask_wtf import FlaskForm # wtf part
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL, InputRequired

class CafeForm(FlaskForm):  # wtf part too
  cafe = StringField(label='Cafe name', validators=[InputRequired(), DataRequired()])
  location = URLField(label='Cafe Location on Google Maps', validators=[InputRequired(), URL(allow_ip=False,
  message="Invalid address")])
  open = StringField(label='Opening Time e.g. 8AM', validators=[InputRequired(), DataRequired()])
  close = StringField(label='Closing Time e.g. 5:30PM', validators=[InputRequired(), DataRequired()])
  coffee = SelectField(label='Coffee Rating', id="coffee", validate_choice=True, choices=['', '☕️', '☕️☕️', '☕️☕️☕️',
  '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️', '✘'], validators=[InputRequired(), DataRequired()])
  # coffee = StringField(label='Coffee Rating', id="coffee", render_kw ={"list":"coffee"}, validators=[InputRequired(),
  # DataRequired()]) # choose items from <datalist> in base.html
  wifi = SelectField(label='Wifi Strength Rating', id="wifi", validate_choice=True, choices=['', '💪', '💪💪',
  '💪💪💪', '💪💪💪💪', '💪💪💪💪💪', '✘'], validators=[InputRequired(), DataRequired()])
  power = SelectField(label='Power Socket Availability', id="power", validate_choice=True, choices=['', '🔌', '🔌🔌',
  '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌', '✘'], validators=[InputRequired(), DataRequired()])
  # power = StringField('Power Socket Availability', id="power", render_kw ={"list":"power"},
  # validators=[InputRequired(),DataRequired()]) # choose items from <datalist> in add.html
  submit = SubmitField('Submit')

  # those below was cutted from main.py
  # class CafeForm(FlaskForm): #wtf part too
  #     cafe = StringField(label='Cafe name', validators=[InputRequired(),DataRequired()])
  #     location = URLField(label='Cafe Location on Google Maps', validators=[InputRequired(),URL(allow_ip=False, message="Invalid address")])
  #     open = StringField(label='Opening Time e.g. 8AM', validators=[InputRequired(),DataRequired()])
  #     close = StringField(label='Closing Time e.g. 5:30PM', validators=[InputRequired(),DataRequired()])
  #     coffee = SelectField(label='Coffee Rating', id="coffee",validate_choice=True, choices=['','☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️','✘'],validators=[InputRequired(),DataRequired()])
  #     # coffee = StringField(label='Coffee Rating', id="coffee", render_kw ={"list":"coffee"}, validators=[InputRequired(),DataRequired()]) # choose items from <datalist> in base.html
  #     wifi = SelectField(label='Wifi Strength Rating', id="wifi", validate_choice=True, choices=['','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪','✘'], validators=[InputRequired(),DataRequired()])
  #     power = SelectField(label='Power Socket Availability', id="power",validate_choice=True, choices=['','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌','✘'], validators=[InputRequired(),DataRequired()])
  #     # power = StringField('Power Socket Availability', id="power", render_kw ={"list":"power"}, validators=[InputRequired(),DataRequired()]) # choose items from <datalist> in add.html
  #     submit = SubmitField('Submit')