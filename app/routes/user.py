from flask import Blueprint, request

from app.schemas.user import UserSchema
from app.daos.user import user_dao


user_bp = Blueprint("user", __name__)
user_schema = UserSchema()


@user_bp.route("/", methods=["POST"])
def create_user():
    user_json = request.get_json()
    user = user_schema.load(user_json)

    created_user = user_dao.create_user(user)
    return user_schema.dump(created_user), 201