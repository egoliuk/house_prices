# Сервіс для прогнозування вартості будинку.

Опис завдання на [kaggle.com](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

## Архітектура

Цей додаток є веб-сервером, який надає RESTful API для взаємодії.
Для взаємодії з цим RESTful API існує [користувацький інтерфейс](https://github.com/bartoshyk/house-prices-ui)

## Потрібні бібліотеки та інструменти

* Python 3.6
* pip 19.0.3
* Flask 1.0.2
* Flask-WTF
* Jinja2 (залежність Flask)
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-Login
* Werkzeug (залежність Flask)
* scikit-learn

## Опис алгоритму обробки даних та прогнозування

Загальні концепції та техніки Machine Learning, які використовуються для підготовки даних та прогнозування вартості будинку.
//TODO

## Налаштувати оточення

Створити віртуальне оточення
```sh
python3 -m venv venv
```

Активувати віртуальне середовище
```sh
source venv/bin/activate
```

Перевірити версію pip, якщо треба оновити версію
```sh
pip install --upgrade pip
```

Встановити Flask у віртуальне середовище
```sh
pip install flask
```

Задати змінну оточення FLASK_APP
```sh
export FLASK_APP=house_prices.py
```

Встановити Flask-WTF
```sh
pip install flask-wtf
```
Flask-WTF - це розширення до Flask, для роботи за веб-формами. 
Воно є обгорткою навколо WTForms.

Встановити Flask-SQLAlchemy
```sh
pip install flask-sqlalchemy
```
Flask-SQLAlchemy - це розширення для Flask, 
яке є обгорткою для популярного ORM пакета SQLAlchemy.

Встановити Flask-Migrate
```sh
pip install flask-migrate
```
Flask-Migrate - це розширення для Flask, 
яке є обгорткою для Alembic, основи для міграцію біз даних SQLAlchemy.

Встановити Flask-Login
```sh
pip install flask-login
```

Для деактивації віртуального оточення введіть
```sh
deactivate
```

## Запуск

Активувати попередньо налаштоване віртуальне середовище
```sh
source venv/bin/activate
```

Запустити веб додаток
```sh
flask run
```

Для зупинки додатку натисніть `CTRL+C`

Для деактивації віртуального оточення введіть
```sh
deactivate
```
