from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
