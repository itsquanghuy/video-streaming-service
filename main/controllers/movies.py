import os

from flask import send_from_directory

from main import app, config
from main.commons.decorators import (
    parse_args_with,
    require_authorized_phone,
    validate_movie,
)
from main.commons.exceptions import BadRequest
from main.engines.movie import get_movie_count, get_movies
from main.schemas.movie import MoviePaginationSchema, MovieSchema
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


@app.get("/movies/<int:movie_id>")
@require_authorized_phone
@validate_movie
def get_movie_(movie, **__):
    return MovieSchema().jsonify(movie)


@app.get("/movies/<string:movie_uuid>")
@require_authorized_phone
def get_movie_file(movie_uuid, **__):
    return send_from_directory(
        os.path.join(app.root_path, "movies"),
        f"{movie_uuid}.mp4",
    )


@app.get("/movies/<string:movie_uuid>/poster")
# @require_authorized_phone
def get_movie_poster(movie_uuid, **__):
    return send_from_directory(
        os.path.join(app.root_path, "movies"),
        f"{movie_uuid}.jpg",
    )
