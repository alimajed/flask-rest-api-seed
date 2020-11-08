from marshmallow import post_dump, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app.database.db import Session


class BaseModelSchema(SQLAlchemyAutoSchema):
    __envelope__ = {"single": None, "many": None}

    class Meta:
        sqla_session = Session
        load_instance = True

    def get_envelope_key(self, many):
        """Helper to get the envelope key."""
        key = self.__envelope__["many"] if many else self.__envelope__["single"]
        assert key is not None, "Envelope key undefined"
        return key

    @post_dump(pass_many=True)
    def wrap_with_envelope(self, data, many, **kwargs):
        key = self.get_envelope_key(many)
        return {key: data}


class BaseCustomSchema(Schema):

    class Meta:
        pass