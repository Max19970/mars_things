from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired


class PublishForm(FlaskForm):
    file = FileField("Добавьте картинку",
                     validators=[FileRequired(), DataRequired(),
                                 FileAllowed(['png', 'jpg', 'jpeg'],
                                             'Для загрузки допускаются только файлы форматов PNG, JPG, JPEG')])
    submit = SubmitField('Опубликовать')
