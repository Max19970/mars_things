from data.users import User
from data.jobs import Jobs
from data import db_session
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
