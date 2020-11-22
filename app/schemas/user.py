from app.database.models.user import UserModel
from app.schemas.base import BaseModelSchema


class UserSchema(BaseModelSchema):

    class Meta(BaseModelSchema.Meta):
        model = UserModel
        load_only = ("password",)
        dump_only = ("id", "created_at", "updated_at")