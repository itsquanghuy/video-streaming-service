from marshmallow import fields

from main.schemas.base import BaseSchema


class PlaybackCurrentTimeSchema(BaseSchema):
    current_time = fields.Integer(required=True)
