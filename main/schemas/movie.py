from marshmallow import fields

from .base import BaseSchema
from .pagination import PaginationSchema


class MovieSchema(BaseSchema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    uuid = fields.String(required=True)
    release_year = fields.Integer(required=True)
    is_a_series = fields.Boolean(required=True)


class MovieSeriesSchema(BaseSchema):
    class EpisodeSchema(BaseSchema):
        id = fields.Integer(required=True, dump_only=True)
        title = fields.String(required=True)
        description = fields.String(required=True)
        season = fields.Integer(required=True, dump_only=True)
        volume = fields.Integer(required=True, dump_only=True)
        episode = fields.Integer(required=True, dump_only=True)
        uuid = fields.String(required=True)

    class MetadataSchema(BaseSchema):
        season = fields.Integer(required=True, dump_only=True)
        number_of_episodes = fields.Integer(required=True, dump_only=True)

    metadata = fields.List(fields.Nested(MetadataSchema), dump_only=True)
    series = fields.List(fields.Nested(EpisodeSchema), dump_only=True)


class MoviePaginationSchema(PaginationSchema):
    items = fields.List(fields.Nested(MovieSchema), dump_only=True)
