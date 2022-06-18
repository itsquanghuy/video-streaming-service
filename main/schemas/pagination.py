from marshmallow import fields, post_load

from .base import BaseSchema


class PaginationSchema(BaseSchema):
    items_per_page = fields.Integer(required=True, dump_only=True)
    page = fields.Integer(required=True)
    total_items = fields.Integer(required=True, dump_only=True)
