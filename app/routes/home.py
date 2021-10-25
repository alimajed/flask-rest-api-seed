from flask import Blueprint
from flask_jwt_extended import jwt_required


home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def home():
    return "Hello World", 200


@home_bp.route("/protected", methods=["GET"])
@jwt_required( )
def protected_home():
    return "Hello World from Protected", 200