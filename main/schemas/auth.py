from marshmallow import fields

from .base import BaseSchema


class AuthSchema(BaseSchema):
    uuid = fields.String(required=True, load_only=True)
