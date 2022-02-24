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


@app.route('/choice/<planet>')
def choice(planet):
    if planet == 'Меркурий':
        str1 = 'Наиболее близко расположен к Солнцу'
        str2 = 'Получает энергии Солнца в 7 раз больше чем Земля'
        str3 = 'Самая наименьшая планета земной группы'
        str4 = 'Его поверхность схожа с поверхностью Луны'
        str5 = 'У него есть собственное магнитное поле, многократно слабее земного'
    elif planet == 'Венера':
        str1 = 'Венера – соседка Земли в космосе.'
        str2 = 'Венера находится к Земле ближе всех остальных планет нашей Солнечной системы.'
        str3 = 'У Венеры и Земли похожие размеры и масса'
        str4 = 'Атмосфера Венеры более чем на 90% состоит из углекислого газа'
        str5 = 'Горы Максвела считаются благоприятным местом для посадки космических аппаратов.'
    elif planet == 'Марс':
        str1 = 'Атмосфера на Марсе в 100 раз более разряженная, чем на Земле'
        str2 = 'Температура на экваторе Марса колеблется от +30 ºC в полдень и до - 80 ºC в полночь.'
        str3 = 'По сравнению с Землей, на Марсе гравитация в 2,5 раза слабее'
        str4 = 'Во время зимнего периода на планете замерзает около 20% воздуха.'
        str5 = 'Марс имеет почти аналогичный земному период вращения вокруг оси'
    else:
        str1 = '???'
        str2 = '???'
        str3 = '???'
        str4 = '???'
        str5 = '???'
    return f"""
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
                        <title>Варианты выбора</title>
                  </head>
                  <body>
                        <h1>Мое предложение: { planet }</h1>
                        <div class="alert alert-dark" role="alert">
                        <h4>{ str1 }</h4>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <h4>{ str2 }</h4>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <h4>{ str3 }</h4>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h4>{ str4 }</h4>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <h4>{ str5 }</h4>
                    </div>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""
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
                            <title>Результаты</title>
                      </head>
                      <body>
                            <h1>Результаты отбора</h1>
                            <div class="alert alert-dark" role="alert">
                            <h3>Претендента на участие в миссии {nickname}:</h3>
                        </div>
                        <div class="alert alert-success" role="alert">
                          <h4>Поздравляем! Ваш рейтинг после {level} этапа отбора</h4>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          <h4>составляет {rating}!</h4>
                        </div>
                        <div class="alert alert-warning" role="alert">
                          <h3>Желаем удачи!</h3>
                        </div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
