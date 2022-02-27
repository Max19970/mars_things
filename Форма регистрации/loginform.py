from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, IntegerField, EmailField, StringField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = EmailField('Login / Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat password', validators=[DataRequired(),
                                                                   EqualTo('password')])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
