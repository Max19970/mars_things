import os
from flask import Flask, render_template
from werkzeug.utils import secure_filename

from form import PublishForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    form = PublishForm()
    if form.validate_on_submit():
        file = form.file.data
        file.filename = f'{len(os.listdir("static/img")) + 1}.jpg'
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/img', filename))
    images = [(os.listdir('static/img').index(e), e) for e in os.listdir('static/img')]
    return render_template('galery.html', images=images, form=form)


if __name__ == '__main__':
    main()
