from flask import request
from flask_restx import Resource, Namespace
from app.container import genre_service
from app.dao.models.genre import GenreSchema, Genre

genre_ns = Namespace('genres')
genre_schema = GenreSchema()


@genre_ns.route('/')
class GenreView(Resource):
    """Вьюшка вывода всех жанров по ID"""
    def get(self):
        all_genres = genre_service.get_all()
        return genre_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with genre_service.begin():
            genre_service.add(new_genre)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """Вьюшка вывода одного жанра по ID"""
    def get(self, gid: int):
        try:
            genre = genre_service.query(Genre).filter(Genre.id == gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404

    def put(self, gid):
        pass