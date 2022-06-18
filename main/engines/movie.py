from typing import List, Optional

from main.models.movie import MovieModel


def get_movies(page: int, items_per_page: int) -> List[MovieModel]:
    return MovieModel.query.paginate(page, items_per_page, False).items


def get_movie(movie_id: int) -> Optional[MovieModel]:
    return MovieModel.query.get(movie_id)


def get_movie_count() -> int:
    return MovieModel.query.count()
