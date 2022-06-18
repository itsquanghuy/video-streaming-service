from flask import jsonify

from main import app
from main.commons.decorators import parse_args_with
from main.commons.exceptions import Unauthorized
from main.engines.phone import find_phone_by_uuid
from main.libs.jwt import create_access_token
from main.schemas.auth import AuthSchema


@app.post("/auth")
@parse_args_with(AuthSchema())
def authenticate(args):
    phone = find_phone_by_uuid(uuid=args["uuid"])

    if phone is None:
        raise Unauthorized()

    return jsonify(
        access_token=create_access_token(identity=args["uuid"]),
    )
