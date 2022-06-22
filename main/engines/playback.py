from typing import Optional

from sqlalchemy import and_

from main import db
from main.models.movie import EpisodeModel, MovieModel
from main.models.phone import PhoneModel
from main.models.playback import EpisodePlaybackModel, PlaybackModel


def get_playback(phone: PhoneModel, movie: MovieModel) -> Optional[PlaybackModel]:
    return PlaybackModel.query.filter(
        and_(PlaybackModel.phone_id == phone.id, PlaybackModel.movie_id == movie.id)
    ).first()


def set_movie_playback_current_time(
    phone: PhoneModel, movie: MovieModel, current_time: int = 0
) -> None:
    playback = get_playback(phone, movie)

    if playback:
        playback.current_time = current_time
    else:
        playback = PlaybackModel(phone_id=phone.id, movie_id=movie.id)
        db.session.add(playback)

    db.session.commit()


def get_episode_playback(
    phone: PhoneModel, episode: EpisodeModel
) -> Optional[EpisodePlaybackModel]:
    return EpisodePlaybackModel.query.filter(
        and_(
            EpisodePlaybackModel.phone_id == phone.id,
            EpisodePlaybackModel.episode_id == episode.id,
        )
    ).first()


def set_episode_playback_current_time(
    phone: PhoneModel, episode: EpisodeModel, current_time: int = 0
) -> None:
    playback_episode = get_episode_playback(phone, episode)

    if playback_episode:
        playback_episode.current_time = current_time
    else:
        playback_episode = EpisodePlaybackModel(
            phone_id=phone.id, episode_id=episode.id
        )
        db.session.add(playback_episode)

    db.session.commit()
