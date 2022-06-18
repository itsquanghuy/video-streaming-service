from flask_admin.contrib.sqla import ModelView

from main import admin, db
from main.models.playback import PlaybackModel


class PlaybackModelView(ModelView):
    can_create = False


playback_model_view = PlaybackModelView(
    PlaybackModel,
    db.session,
    name="Playback",
)

admin.add_view(playback_model_view)
