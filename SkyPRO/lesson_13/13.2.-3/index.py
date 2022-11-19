import os
import dotenv
from flask import Flask

app = Flask(__name__)

# загружаем в переменные окружения данные из файла .env
dotenv.load_dotenv(override=True)

# В зависимости от значения APP_CONFIG подключаем тот или другой конфиг
if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile("config/development.py")
elif os.environ.get("APP_CONFIG") == "production":
    app.config.from_pyfile("config/production.py")



@app.route('/')
def main_list():
    title = app.config.get('TITLE')
    description = app.config.get('DESCRIPTION')

    return f'<h1>{title}</h1><p>{description}</p>'

app.run()
