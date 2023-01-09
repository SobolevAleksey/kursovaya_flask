from flask import Flask
from main.views import main_blueprint
from api.views import api_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def not_found_error(error):
    return 'Страница не найдена!', 404


@app.errorhandler(500)
def not_found_error_server(error):
    return 'Ошибка на сервере!', 500


if __name__ == "__main__":
    app.run(debug=True)
