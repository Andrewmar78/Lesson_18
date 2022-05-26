from typing import List
from app.dao.models.movie import Movie, MovieSchema
# from exceptions import EntityNotFound


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        # movies = Movie.query.all()
        # return movies
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_filters(self, filters: dict) -> List[Movie]:
        movies = self.session.query(Movie)

        if filters['director_id']:
            movies = movies.filter(Movie.director_id == filters['director_id'])
        if filters['genre_id']:
            movies = movies.filter(Movie.genre_id == filters['genre_id'])
        if filters['year']:
            movies = movies.filter(Movie.year == filters['year'])
        # if movies is None:
        #     raise EntityNotFound

        return movies.all()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    # def update_partial(self, data):
    #     mid = data.get("id")
    #     movie = self.get_one(mid)
    #     if "title" in data:
    #         movie.title = data.get("title")
    #     if "description" in data:
    #         movie.description = data.get("description")
    #     if "trailer" in data:
    #         movie.trailer = data.get("trailer")
    #     if "year" in data:
    #         movie.year = data.get("year")
    #     if "rating" in data:
    #         movie.rating = data.get("rating")
    #     if "genre_id" in data:
    #         movie.genre_id = data.get("genre_id")
    #     if "director_id" in data:
    #         movie.director_id = data.get("director_id")
    #
    #     self.session.add(movie)
    #     self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
