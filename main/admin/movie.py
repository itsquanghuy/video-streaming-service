from main import admin, db
from main.models.movie import EpisodeModel, MovieModel

from .view import ModelView

movie_model_view = ModelView(
    MovieModel,
    db.session,
    name="Movie",
)

episode_model_view = ModelView(EpisodeModel, db.session, name="Movie Episodes")

admin.add_view(movie_model_view)
admin.add_view(episode_model_view)
