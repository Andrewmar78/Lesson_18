from flask import Flask
from flask_restx import Api

from app.config import Config
from app.dao.models.director import Director
from app.dao.models.genre import Genre
from app.dao.models.movie import Movie
from app.setup_db import db
from app.views.movies import movie_ns, director_ns, genre_ns


# функция создания основного объекта app

def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    # configure_app(app)
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    # create_data(app, db)


# функция
# def create_data(app, db):
# Добавляет в базу без запуска приложения
#     with app.app_context():
#         db.create_all()
#         создать несколько сущностей чтобы добавить их в БД
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
# app = create_app(Config())
# app.debug = True

def create_data():

    db.create_all()

    m1 = Movie(title="Оно", description="Веселый клоун убивает детей. А дети убивают его",
               trailer="https://www.youtube.com/watch?v=UKei_d0cbP4", year=1995, rating=8.8, genre_id=11,
               director_id=21)
    m2 = Movie(title="Оно 2", description="Веселый клоун снова очнулся и убивает детей. Но дети опять убивают его",
               trailer="https://www.youtube.com/watch?v=UKei_d0cbP4", year=1999, rating=8.9, genre_id=11,
               director_id=21)

    d1 = Director(name="Неизвестный мужик 2")

    g1 = Genre(name="Новый жанр")

    with db.session.begin():
        db.session.add_all([m1, m2, g1, d1])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    create_data()
    # app.run()
    app.run(host="localhost", port=10001)
