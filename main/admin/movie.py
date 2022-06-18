from flask_admin.contrib.sqla import ModelView

from main import admin, db
from main.models.movie import MovieModel

movie_model_view = ModelView(
    MovieModel,
    db.session,
    name="Movie",
)

admin.add_view(movie_model_view)
