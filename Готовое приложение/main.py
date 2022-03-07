from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from data import db_session
import datetime as dt

from forms.user import RegisterForm, LoginForm, JobsForm
from data.users import User
from data.jobs import Jobs
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/users.db")
    app.run()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
@app.route('/index/')
@app.route('/<title>')
@app.route('/index/<title>')
def index(title='Main page'):
    return render_template('base_title.html', title=title)


@app.route('/works_log')
def works_log():
    db_session.global_init('db/users.db')
    db_sess = db_session.create_session()
    jobs = []
    for job in db_sess.query(Jobs).all():
        team_leader = db_sess.query(User).filter(User.id == job.team_leader)
        team_leader = f'{team_leader[0].surname} {team_leader[0].name}'
        jobs.append((job, team_leader))
    return render_template('works_log.html', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/works_log")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add_job',  methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            job=form.job.data,
            team_leader=form.team_leader.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            start_date=dt.datetime.now(),
            is_finished=form.is_finished.data,
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/works_log')
    return render_template('add_job.html', title='Добавление работы',
                           form=form)


@app.route('/job/<int:job_id>', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == job_id,
                                         (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                         ).first()
        if job:
            form.job.data = job.job
            form.team_leader.data = job.team_leader
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == job_id,
                                         (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                         ).first()
        if job:
            job.job = form.job.data
            job.team_leader = form.team_leader.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/works_log')
        else:
            abort(404)
    return render_template('add_job.html',
                           title='Редактирование работы',
                           form=form
                           )


@app.route('/job_delete/<int:job_id>', methods=['GET', 'POST'])
@login_required
def news_delete(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == job_id,
                                     (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                     ).first()
    if job:
        db_sess.delete(job)
        jobs = []
        for job in db_sess.query(Jobs).all():
            jobs.append(job)
        for job in db_sess.query(Jobs).all():
            job.id = jobs.index(job) + 1  # Обновление индексов работ после изменений
            db_sess.commit()
        db_sess.commit()
    else:
        abort(404)
    return redirect('/works_log')


if __name__ == '__main__':
    main()