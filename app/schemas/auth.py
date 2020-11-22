from marshmallow import fields

from app.schemas.base import BaseCustomSchema
from app.schemas.user import UserSchema


class AuthCredentialSchema(BaseCustomSchema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    

class AuthResponseSchema(BaseCustomSchema):
    access_token = fields.Str(required=True)
    user = fields.Nested(UserSchema)