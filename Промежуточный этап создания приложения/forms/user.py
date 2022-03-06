from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField,\
    BooleanField, StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
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


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class JobsForm(FlaskForm):
    team_leader = IntegerField("Заведующий работой", validators=[DataRequired()])
    job = StringField("Название работы", validators=[DataRequired()])
    work_size = IntegerField("Продолжительность работы (в часах)", validators=[DataRequired()])
    collaborators = StringField("ID Сотрудников", validators=[DataRequired()])
    is_finished = BooleanField("Работа выполнена")
    submit = SubmitField('Применить')