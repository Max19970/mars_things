from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css"
                    href="static/css/style.css">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png"></br>
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронафтов</title>
                          </head>
                          <body>
                                <h1 align='center'>Анкета претендента</h1>
                                <h3 align='center'>на участие в миссии</h3>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" placeholder="Введите фамилию" class="form-control" name="surname" id="surname">
                                        <input type="text" placeholder="Введите имя" class="form-control" name="name" id="name">
                                        <input type="email" placeholder="Введите адрес почты" class="form-control" name="email" id="email">
                                        <div class="formbuilder-select form-group field-educations">
                                            <label for="educations" class="formbuilder-select-label">Какое у вас образование?</label>
                                            <select class="form-control" name="education" id="education">
                                                <option value="Начальное" selected="true" id="Начальное">Начальное</option>
                                                <option value="Общее" id="Общее">Общее</option>
                                                <option value="Среднее" id="Среднее">Среднее</option>
                                                <option value="Высшее" id="Высшее">Высшее</option>
                                            </select>
                                        </div>
                                        <div class="formbuilder-checkbox-group form-group field-jobs">
                                            <label for="jobs" class="formbuilder-checkbox-group-label">Какие у вас есть профессии?</label>
                                            <div class="checkbox-group">
                                                <input name="job" value="Инженер-исследователь" type="checkbox">Инженер-исследователь</input>
                                                <input name="job" value="Инженер-строитель" type="checkbox">Инженер-строитель</input>
                                                <input name="job" value="Пилот" type="checkbox">Пилот</input>
                                                <input name="job" value="Метеоролог" type="checkbox">Метеоролог</input>
                                                <input name="job" value="Инженер по жизнеобеспечению" type="checkbox">Инженер по жизнеобеспечению</input>
                                                <input name="job" value="Инженер по радиационной защите" type="checkbox">Инженер по радиационной защите</input>
                                                <input name="job" value="Врач" type="checkbox">Врач</input>
                                                <input name="job" value="Экзобиолог" type="checkbox">Экзобиолог</input>
                                            </div>
                                        </div>
                                        <div class="formbuilder-radio-group form-group field-sex">
                                            <label for="sex" class="formbuilder-radio-group-label">Укажите пол</label>
                                            <div class="radio-group">
                                                <input name="sex" value="Мужской" type="radio">Мужской</input>
                                                <input name="sex" value="Женский" type="radio">Женский</input>
                                            </div>
                                        </div>
                                        <div class="formbuilder-textarea form-group field-about">
                                            <label for="about" class="formbuilder-textarea-label">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea type="textarea" class="form-control" name="about" access="false" id="about"></textarea>
                                        </div>
                                        <div class="formbuilder-file form-group field-file">
                                            <label for="file" class="formbuilder-file-label">Приложите фотографию</label>
                                            <input type="file" class="form-control" name="file" access="false" multiple="false" id="file">
                                        </div>
                                        <div class="formbuilder-checkbox-group form-group field-ready">
                                            <label for="checkbox-group-1645617319137" class="formbuilder-checkbox-group-label"></label>
                                            <div class="checkbox-group">
                                                <div class="formbuilder-checkbox">
                                                    <input name="ready" value="ready" type="checkbox">
                                                    <label for="accept">Готовы остаться на Марсе?</label>
                                                </div>
                                            </div>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get)
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form.getlist('job'))
        print(request.form['sex'])
        print(request.form['about'])
        print(True if request.form.get('ready') else False)
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
