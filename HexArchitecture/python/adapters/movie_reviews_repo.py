from typing import List
from python.domain.movie_review import MovieReview
from python.domain.movie_search_request import MovieSearchRequest
from python.ports.i_fetch_movie_reviews import iFetchMovieReviews


class MovieReviewsRepo(iFetchMovieReviews):
    def __init__(self):
        self.movieReviewMap = {}
        self.initialize()


    def fetchMovieReviews(self, movieSearchRequest: MovieSearchRequest) -> List[MovieReview]:
        return self.movieReviewMap.get(movieSearchRequest.movieName, [])

    def initialize(self):
        self.movieReviewMap = {
            "StarWars": [MovieReview("1", 7.5, "Good")],
            "StarTreck": [MovieReview("1", 9.5, "Excellent"), MovieReview("1", 8.5, "Good")]
        }