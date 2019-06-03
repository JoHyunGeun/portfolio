from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User
from flask_login import current_user


class ClassificationForm(FlaskForm):

    username = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    picture = FileField('Picture For Diagnosis', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Submit')
