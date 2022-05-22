from flask import request
from flask_restx import Resource, Namespace
from app.container import movie_service, director_service
from app.dao.models.director import DirectorSchema, Director


director_ns = Namespace('directors')
director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorView(Resource):
    """Вьюшка вывода всех режиссеров по ID"""
    def get(self):
        all_directors = director_service.get_all()
        return director_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with director_service.begin():
            director_service.add(new_director)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    """Вьюшка вывода одного режиссера по ID"""
    def get(self, did: int):
        try:
            director = director_service.query(Director).filter(Director.id == did)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404

    def put(self, did):
        pass
