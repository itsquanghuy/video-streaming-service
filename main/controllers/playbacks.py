from flask import jsonify

from main import app
from main.commons.decorators import (
    parse_args_with,
    require_authorized_phone,
    validate_movie,
    validate_movie_episode,
)
from main.commons.exceptions import BadRequest
from main.engines.playback import (
    get_episode_playback,
    get_playback,
    set_episode_playback_current_time,
    set_movie_playback_current_time,
)
from main.schemas.playback import PlaybackCurrentTimeSchema


@app.get("/playbacks/<string:movie_uuid>/current-time")
@require_authorized_phone
@validate_movie
def get_playback_(phone, movie, **__):
    playback = get_playback(phone, movie)

    if playback is None:
        set_movie_playback_current_time(phone, movie)
        playback = get_playback(phone, movie)

    return PlaybackCurrentTimeSchema().jsonify(playback)


@app.put("/playbacks/<string:movie_uuid>/current-time")
@require_authorized_phone
@validate_movie
@parse_args_with(PlaybackCurrentTimeSchema())
def set_current_time(phone, movie, args, **__):
    current_time = args["current_time"]

    if current_time < 0:
        raise BadRequest(error_message="Playback current time cannot be negative.")

    set_movie_playback_current_time(phone, movie, current_time=current_time)

    return jsonify({})


@app.get("/playbacks/episodes/<string:episode_uuid>/current-time")
@require_authorized_phone
@validate_movie_episode
def get_episode_playback_(phone, episode, **__):
    playback = get_episode_playback(phone, episode)

    if playback is None:
        set_movie_playback_current_time(phone, episode)
        playback = get_episode_playback(phone, episode)

    return PlaybackCurrentTimeSchema().jsonify(playback)


@app.put("/playbacks/episodes/<string:episode_uuid>/current-time")
@require_authorized_phone
@validate_movie_episode
@parse_args_with(PlaybackCurrentTimeSchema())
def set_episode_current_time(phone, episode, args, **__):
    current_time = args["current_time"]

    if current_time < 0:
        raise BadRequest(error_message="Playback current time cannot be negative.")

    set_episode_playback_current_time(phone, episode, current_time=current_time)

    return jsonify({})
