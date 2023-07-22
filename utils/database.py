import requests
from utils.constants import *


def get_non_rated_movie():
    movies = requests.get(MOVIES_URL)
    ratings = requests.get(RATINGS_URL)

    if movies.ok and ratings.ok:
        movies = movies.json()
        ratings = ratings.json()

        rated_movies = set(rating["movie_id"] for rating in ratings)
        print("Rated movies:", rated_movies)

        # This should put the best movies in the end
        movies.reverse()
        movie = None
        genres = []
        eligible_movie_found = False
        while len(movies) > 0 and not eligible_movie_found:
            movie = movies.pop()
            if movie["movie_id"] not in rated_movies:
                movie["genres"] = get_genres_from_movie(movie["movie_id"])
                eligible_movie_found = True
        print("Selected movie:", movie)
        return movie


def get_genres_from_movie(movie_id):
    genres = requests.get(GENRES_BY_MOVIE_URL + str(movie_id))
    print("Genres:", genres.status_code, genres.json())
    return genres.json()