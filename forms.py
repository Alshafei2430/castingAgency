
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SelectMultipleField, DateTimeField, DateField
from wtforms.validators import DataRequired, AnyOf, URL

class ActorForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    age = IntegerField(
        'age', validators=[DataRequired()]
    )
    gender = StringField(
        'gender', validators=[DataRequired()]
    )
class MovieForm(FlaskForm):
    title = StringField(
        'title', validators=[DataRequired()]
    )
    release_date = DateField(
        'release_date', validators=[DataRequired()],
        default= datetime.today()
    )