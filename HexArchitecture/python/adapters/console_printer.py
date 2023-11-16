
from typing import List
from python.domain.movie_review import MovieReview
from python.ports.i_print_movie_rewiews import iPrintMovieReviews


class ConsolePrinter(iPrintMovieReviews):
    def writeMovieReviews(self, movieReviewList: List[MovieReview]):
        for movieReview in movieReviewList:
          print(movieReview)






