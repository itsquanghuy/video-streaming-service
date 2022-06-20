from typing import Dict, List, Optional

from sqlalchemy import and_

from main import db
from main.models.movie import MovieModel, MovieSeriesModel


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


def get_movie_series_metadata(movie: MovieModel) -> List[Dict[int, int]]:
    results = (
        db.session.query(
            MovieSeriesModel.season,
            db.func.count(MovieSeriesModel.episode).label("number_of_episodes"),
        )
        .join(
            MovieModel,
            and_(
                MovieModel.id == MovieSeriesModel.movie_id,
                MovieModel.uuid == movie.uuid,
            ),
        )
        .group_by(MovieSeriesModel.season)
        .all()
    )
    return [dict(result) for result in results]
