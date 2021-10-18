from os import access
from flask import Blueprint, request

from app.daos.user import user_dao
from app.schemas.user import UserSchema
from app.schemas.auth import AuthCredentialSchema, AuthResponseSchema


auth_bp = Blueprint("auth", __name__)
user_schema = UserSchema()
auth_creds_schema = AuthCredentialSchema()
auth_response_schema = AuthResponseSchema()


@auth_bp.route("/", methods=['POST'])
def authenticate():
    auth_creds_json = request.get_json()
    auth_creds = auth_creds_schema.load(auth_creds_json)

    user, access_token = user_dao.authenticate(auth_creds)
    return auth_response_schema.dump({
        "access_token": access_token,
        "user": user
    }), 200
