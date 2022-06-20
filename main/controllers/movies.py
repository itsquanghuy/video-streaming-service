import os

from flask import send_from_directory

from main import app, config
from main.commons.decorators import (
    parse_args_with,
    require_authorized_phone,
    validate_movie,
)
from main.commons.exceptions import BadRequest
from main.engines.movie import get_movie_count, get_movie_series_metadata, get_movies
from main.schemas.movie import MoviePaginationSchema, MovieSchema, MovieSeriesSchema
from main.schemas.pagination import PaginationSchema


@app.get("/movies")
@require_authorized_phone
@parse_args_with(PaginationSchema())
def index(args, **__):
    page = args["page"]

    if page < 1:
        raise BadRequest(error_message="Can't get items from page 0.")

    movies = get_movies(
        page=page,
        items_per_page=config.ITEMS_PER_PAGE,
    )

    return MoviePaginationSchema().jsonify(
        {
            "items_per_page": config.ITEMS_PER_PAGE,
            "page": page,
            "total_items": get_movie_count(),
            "items": movies,
        }
    )


@app.get("/movies/<string:movie_uuid>")
@require_authorized_phone
@validate_movie
def get_movie_(movie, **__):
    return MovieSchema().jsonify(movie)


@app.get("/movies/<string:movie_uuid>/series")
@require_authorized_phone
@validate_movie
def get_movie_series(movie, **__):
    if not movie.is_a_series:
        raise BadRequest(error_message="This movie is not a movie series.")

    metadata = get_movie_series_metadata(movie)

    return MovieSeriesSchema().jsonify(
        {
            "metadata": metadata,
            "series": sorted(movie.series, key=lambda episode: episode.uuid),
        }
    )


@app.get("/movies/<string:movie_uuid>/media")
@require_authorized_phone
def get_movie_file(movie_uuid, **__):
    return send_from_directory(
        os.path.join(app.root_path, "movies"),
        f"{movie_uuid}.mp4",
    )


@app.get("/movies/<string:movie_uuid>/poster")
def get_movie_poster(movie_uuid, **__):
    return send_from_directory(
        os.path.join(app.root_path, "movies"),
        f"{movie_uuid}.jpg",
    )
