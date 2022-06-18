import os

from flask import send_from_directory

from main import app, config
from main.commons.decorators import parse_args_with, validate_movie, require_authorized_phone
from main.engines.movie import get_movies, get_movie_count
from main.schemas.pagination import PaginationSchema
from main.schemas.movie import MoviePaginationSchema, MovieSchema
from main.commons.exceptions import BadRequest


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

    return MoviePaginationSchema().jsonify({
        "items_per_page": config.ITEMS_PER_PAGE,
        "page": page,
        "total_items": get_movie_count(),
        "items": movies,
    })


@app.get("/movies/<int:movie_id>")
@require_authorized_phone
@validate_movie
def get_movie_(movie, **__):
    return MovieSchema().jsonify(movie)


@app.get("/movies/<string:movie_uuid>")
@require_authorized_phone
def get_movie_file(movie_uuid, **__):
    # Enforce user not to download the file on the web
    # response = make_response()
    # response.headers["Content-Disposition"] = "video/mp4; filename=test.mp4;"
    # response.headers["Content-Type"] = "application/mp4"
    # with open(os.path.join(app.root_path, "static", "movies", filename), "rb") as f:
    #     response.data = f.read()
    # return response

    return send_from_directory(os.path.join(app.root_path, "static", "movies"), f"{movie_uuid}.mp4")