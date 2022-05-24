from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_one_by_all(self, filters: dict):
        return self.dao.get_one_by_all(filters)

    # def get_all_by_director(self):
    #     all_movies = self.dao.get_all()
    #     director_id = request.args.get('director_id')
    #     if director_id:
    #         all_movies = self.dao.query(Movie).filter(Movie.director_id == director_id)
    #     return self.dao.get_all_by_director(mid)

    # def get_all_by_genre(self, mid):
    #     return self.dao.get_all_by_genre(mid)
    #
    # def get_all_by_year(self, mid):
    #     return self.dao.get_all_by_year(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)
        movie.title = data.get("title")
        # Остальные поля аналогично
        self.dao.update(data)

    def update_partial(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)
        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        # Остальное можно добавить аналогично
        self.dao.update(movie)
        # self.session.add(movie)
        # self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
