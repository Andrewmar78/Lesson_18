from flask import request
from flask_restx import Resource, Namespace
from app.container import movie_service, director_service
from app.dao.models.director import DirectorSchema, Director


director_ns = Namespace('directors')
director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsView(Resource):
    """Вьюшка вывода всех режиссеров"""
    def get(self):
        all_directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(all_directors)
        return result, 200

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
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        # Изменить на обработку конкретной ошибки
        except Exception as e:
            return str(e), 404

    def put(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    def delete(self, mid):
        director_service.delete(mid)
        return "", 204
