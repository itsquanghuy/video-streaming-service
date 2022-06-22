from typing import Dict, List, Optional

from sqlalchemy import and_

from main import db
from main.models.movie import EpisodeModel, MovieModel


def get_movies(page: int, items_per_page: int) -> List[MovieModel]:
    return (
        MovieModel.query.order_by(MovieModel.title)
        .order_by(MovieModel.release_year)
        .paginate(page, items_per_page, False)
        .items
    )


def get_movie(movie_uuid) -> Optional[MovieModel]:
    return MovieModel.query.filter(MovieModel.uuid == movie_uuid).first()


def get_movie_count() -> int:
    return MovieModel.query.count()


def get_movie_series_episode(episode_uuid: str) -> EpisodeModel:
    return EpisodeModel.query.filter(EpisodeModel.uuid == episode_uuid).first()


def get_movie_series_metadata(movie: MovieModel) -> List[Dict[int, int]]:
    results = (
        db.session.query(
            EpisodeModel.season,
            db.func.count(EpisodeModel.volume).label("number_of_episodes"),
        )
        .join(
            MovieModel,
            and_(
                MovieModel.id == EpisodeModel.movie_id,
                MovieModel.uuid == movie.uuid,
            ),
        )
        .group_by(EpisodeModel.season)
        .all()
    )
    return [dict(result) for result in results]
