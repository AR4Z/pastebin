from marshmallow import fields, Schema, ValidationError, validate


class Paste(Schema):
    _id = fields.Str(required=True)
    title = fields.Str(required=False)
    text = fields.Str(required=True)
    time_expiration = fields.Str(required=True)
    date_expiration = fields.Str(required=True, format='%Y-%m-%d %H:%M:%S')
