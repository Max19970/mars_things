import os
from flask import Flask, render_template, redirect, request
from werkzeug.utils import secure_filename

from form import PublishForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    form = PublishForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/img', filename))
        image = f'/static/img/{filename}'
    else:
        image = None
    return render_template('load_photo.html', form=form, image=image)


if __name__ == '__main__':
    main()
