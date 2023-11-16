from python.application.movie_app import MovieApp
from python.domain.model import Model
from python.ports.i_fetch_movie_reviews import iFetchMovieReviews
from python.ports.i_print_movie_rewiews import iPrintMovieReviews
from python.ports.i_user_input import iUserInput


class UserCommand(iUserInput):
    def init(self, fetchMovieReviews: iFetchMovieReviews, printMovieReviews: iPrintMovieReviews):
        movieApp = MovieApp(fetchMovieReviews, printMovieReviews)
        self.model = Model(movieApp)


    def handleUserInput(self, userCommand):
        self.model.Run(userCommand)