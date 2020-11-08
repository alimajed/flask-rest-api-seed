from app.database.models.user import UserModel
from app.schemas.base import BaseModelSchema


class UserSchema(BaseModelSchema):
    __envelope__ = {"single": "user", "many": "users"}

    class Meta(BaseModelSchema.Meta):
        model = UserModel
        load_only = ((),)
        dump_only = ("id", "created_at", "updated_at")