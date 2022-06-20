from main import admin, db
from main.models.movie import MovieModel, MovieSeriesModel

from .view import ModelView

movie_model_view = ModelView(
    MovieModel,
    db.session,
    name="Movie",
)

movie_series_model_view = ModelView(MovieSeriesModel, db.session, name="Movie Series")

admin.add_view(movie_model_view)
admin.add_view(movie_series_model_view)
