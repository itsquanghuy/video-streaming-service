from functools import wraps

from flask import request
from marshmallow import ValidationError

from main.commons.exceptions import BadRequest, NotFound, Unauthorized
from main.engines.movie import get_movie
from main.engines.phone import find_phone_by_uuid
from main.libs.jwt import get_jwt_data, get_jwt_token


def get_request_args():
    if request.method == "GET":
        return request.args.to_dict()
    return request.get_json() or {}


def parse_args_with(schema):
    """
    This decorator can be used to parse
    arguments of a request using a Marshmallow schema.
    If there is any validation error,
    a BadRequest exception will be raised along with the error details.
    """

    def parse_args_with_decorator(f):
        @wraps(f)
        def decorated_function(**kwargs):
            request_args = get_request_args()
            try:
                parsed_args = schema.load(request_args)
            except ValidationError as exc:
                raise BadRequest(error_message=exc.messages)
            kwargs["args"] = parsed_args
            return f(**kwargs)

        return decorated_function

    return parse_args_with_decorator


def validate_movie(f):
    @wraps(f)
    def wrapper(**kwargs):
        movie_uuid = kwargs["movie_uuid"]

        movie = get_movie(movie_uuid)

        if movie is None:
            raise NotFound(error_message=f"Movie with uuid {movie_uuid} not found.")

        kwargs["movie"] = movie

        return f(**kwargs)

    return wrapper


def require_authorized_phone(f):
    @wraps(f)
    def wrapper(**kwargs):
        token = get_jwt_token()
        data = get_jwt_data(token)

        if data:
            phone = find_phone_by_uuid(data["iss"])

            if phone:
                kwargs["phone"] = phone
                return f(**kwargs)

        raise Unauthorized()

    return wrapper
