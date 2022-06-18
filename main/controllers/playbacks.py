from flask import jsonify

from main import app
from main.commons.decorators import parse_args_with, validate_movie, require_authorized_phone
from main.engines.playback import set_movie_playback_current_time, get_playback
from main.schemas.playback import PlaybackCurrentTimeSchema
from main.commons.exceptions import BadRequest


@app.get("/playbacks/<int:movie_id>/current-time")
@require_authorized_phone
@validate_movie
def get_playback_(phone, movie, **__):
    playback = get_playback(phone, movie)

    if playback is None:
        set_movie_playback_current_time(phone, movie)
        playback = get_playback(phone, movie)

    return PlaybackCurrentTimeSchema().jsonify(playback)


@app.put("/playbacks/<int:movie_id>/current-time")
@require_authorized_phone
@validate_movie
@parse_args_with(PlaybackCurrentTimeSchema())
def set_current_time(phone, movie, args, **__):
    current_time = args["current_time"]

    if current_time < 0:
        raise BadRequest(error_message="Playback current time cannot be negative.")

    set_movie_playback_current_time(phone, movie, current_time=current_time)

    return jsonify({})
