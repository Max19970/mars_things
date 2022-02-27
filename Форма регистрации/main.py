from data.users import User
from flask import Flask, render_template, redirect, request
from loginform import LoginForm
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_user(form):
    db_session.global_init('db/users.db')
    db_sess = db_session.create_session()
    user = User()
    user.email = form['email']
    user.surname = form['surname']
    user.name = form['name']
    user.age = form['age']
    user.position = form['position']
    user.speciality = form['speciality']
    user.address = form['address']
    db_sess.add(user)
    db_sess.commit()
    db_sess.close()


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base_title.html', title=title)


@app.route('/register', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        add_user(request.form)
        return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
