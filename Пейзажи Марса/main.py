from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


if __name__ == '__main__':
    main()
