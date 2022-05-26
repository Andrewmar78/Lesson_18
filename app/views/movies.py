from flask import request
from flask_restx import Resource, Namespace
from app.container import movie_service
from app.dao.models.director import DirectorSchema
from app.dao.models.genre import GenreSchema
from app.dao.models.movie import MovieSchema, Movie


movie_ns = Namespace('movies')
director_ns = Namespace('directors')
genre_ns = Namespace('genres')

movie_schema = MovieSchema()
director_schema = DirectorSchema()
genre_schema = GenreSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Получаем все фильмы по режиссеру, жанру и/или году"""
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {'director_id': director_id, 'genre_id': genre_id, 'year': year}

        all_movies = movie_service.get_by_filters(filters)
        result = MovieSchema(many=True).dump(all_movies)
        return result, 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with movie_service.begin():
            movie_service.add(new_movie)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """Вьюшка вывода одного фильма по ID"""
    def get(self, mid: int):
        # try:
            # movie = movie_service.query(Movie).filter(Movie.id == mid)
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        # except Exception as e:
        #     return str(e), 404

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204
