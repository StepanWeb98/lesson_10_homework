from flask import Flask
# Импортируем блюпринт
from app.main.views import main_blueprint

# Создаем экземпляр Flask
app = Flask(__name__)

# регистрируем первый блюпринт
app.register_blueprint(main_blueprint)

# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()
