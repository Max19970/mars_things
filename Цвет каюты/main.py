from flask import Flask, render_template, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base_title.html', title=title)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    data = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда хотел застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', **data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    data = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
            'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', data=data)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
