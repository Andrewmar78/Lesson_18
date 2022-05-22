from app.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all_by_director(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all_by_genre(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all_by_year(self, mid):
        return self.session.query(Movie).get(mid)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)
        movie.title = data.get("title")
        self.session.add(movie)
        self.session.commit()

    def update_partial(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)
        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        # Остальное можно добавить аналогично
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
