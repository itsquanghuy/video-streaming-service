from main import admin, db
from main.models.movie import MovieModel

from .view import ModelView

movie_model_view = ModelView(
    MovieModel,
    db.session,
    name="Movie",
)

admin.add_view(movie_model_view)
