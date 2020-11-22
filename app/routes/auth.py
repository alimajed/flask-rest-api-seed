from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.database.models.user import UserModel
from app.schemas.user import UserSchema
from app.schemas.auth import AuthCredentialSchema, AuthResponseSchema
from app.herlpers.localization import gettext


auth_bp = Blueprint("auth", __name__)
user_schema = UserSchema()
auth_creds_schema = AuthCredentialSchema()
auth_response_schema = AuthResponseSchema()


@auth_bp.route("/", methods=['POST'])
def authenticate():
    auth_creds_json = request.get_json()
    auth_creds = auth_creds_schema.load(auth_creds_json)

    user = UserModel.find_by_email(auth_creds["email"])

    if user and user.is_correct_password(auth_creds["password"]):
        access_token = create_access_token(identity=user.email)
        user_json = user_schema.dump(user)
        print(user_json)
        return auth_response_schema.dump({
            "access_token": access_token,
            "user": user
        }), 200

    return {"message": gettext("wrong_credentials")}, 401
