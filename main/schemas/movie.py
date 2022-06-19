from marshmallow import fields

from .base import BaseSchema
from .pagination import PaginationSchema


class MovieSchema(BaseSchema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    uuid = fields.String(required=True)
    release_year = fields.Integer(required=True)


class MoviePaginationSchema(PaginationSchema):
    items = fields.List(fields.Nested(MovieSchema), dump_only=True)
