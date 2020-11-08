from flask import Blueprint, request

from app.database.models.user import UserModel
from app.schemas.user import UserSchema
from app.herlpers.localization import gettext


user_bp = Blueprint("user", __name__)
user_schema = UserSchema()


@user_bp.route("/", methods=["POST"])
def create_user():
    user_json = request.get_json()
    user = user_schema.load(user_json)

    if UserModel.find_by_email(user.email):
        return {"message": gettext("user_exists")}, 409
    
    user.save_to_db()
    return user_schema.dump(user), 201