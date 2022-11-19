# Сперва импортируем Flask
from flask import Flask

# Затем создадим экземпляр этого Flask, назовем его app -
# это будет наше приложение

app = Flask(__name__)

# Что такое __name__ ?
# При запуске сценария значение переменной __name__ равно __main__
# Эта переменная помогает Flask разбираться, где он находится
# и без нее он просто не заработает

# Теперь создадим функцию, которая будет что-то делать
# Например, page_index — это функция, которая будет возвращать 'Hello World!'

def page_index():
   return "Hello World!"

# Теперь используем метод у приложения, который зарегистрирует маршрут
# Например, для главной страницы будет вызвана функция page_index

app.add_url_rule('/',view_func=page_index)

#Теперь стартуем сервер, чтобы обрабатывать запросы от пользователей

app.run()
