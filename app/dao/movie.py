from typing import List
from flask import request
from app.dao.models.movie import Movie, MovieSchema


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        # movies = Movie.query.all()
        # return movies
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_one_by_all(self, filters: dict) -> List[Movie]:
        movies = self.session.query(Movie).all()

        if filters['director_id']:
            movies = movies.filter(Movie.director_id == filters['director_id'])
        if filters['genre_id']:
            movies = movies.filter(Movie.genre_id == filters['genre_id'])
        if filters['year']:
            movies = movies.filter(Movie.year == filters['year'])

        return movies.all()

    # def get_all_by_director(self):
    #     all_movies = self.session.get_all()
    #     director_id = request.args.get('director_id')
    #     if director_id:
    #         all_movies = self.session.query(Movie).filter(Movie.director_id == director_id)
    #     return all_movies

    # def get_all_by_genre(self, mid):
    #     return self.session.query(Movie).get(mid)
    #
    # def get_all_by_year(self, mid):
    #     return self.session.query(Movie).get(mid)

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
