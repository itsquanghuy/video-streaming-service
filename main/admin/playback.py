from main import admin, db
from main.models.playback import EpisodePlaybackModel, PlaybackModel

from .view import ModelView


class PlaybackModelView(ModelView):
    can_create = False


playback_model_view = PlaybackModelView(
    PlaybackModel,
    db.session,
    name="Playback",
)
episode_playback_model_view = PlaybackModelView(
    EpisodePlaybackModel, db.session, name="Episode Playback"
)

admin.add_view(playback_model_view)
admin.add_view(episode_playback_model_view)
