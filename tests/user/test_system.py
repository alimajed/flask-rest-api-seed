import json
from datetime import date

from tests.config import app_inst
from tests.helpers import json_serial
from app.database.models.user import UserModel
from app.daos.user import user_dao


def test_create_user(app_inst):
    with app_inst.test_client() as c:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        user_json = {
            "first_name": "ali",
            "last_name": "majed",
            "date_of_birth": date(1991,3,26),
            "email": "alimajed1991+3@gmail.com",
            "password": "password123"
        }
        req = c.post("http://localhost:5000/api/user/", data=json.dumps(user_json, default=json_serial), headers=headers)
        assert req.status_code == 201


def test_user_sign_in(app_inst):
    with app_inst.test_client() as c:
        user = UserModel("ali", "majed", date(1991,3,26), "alimajed1991+4@gmail.com", "password123")
        user_dao.create_user(user)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        creds = {
            "email": "alimajed1991+4@gmail.com",
            "password": "password123"
        }
        req = c.post("http://localhost:5000/api/auth/", data=json.dumps(creds, default=json_serial), headers=headers)
        assert req.status_code == 200

def test_user_auth(app_inst):
    with app_inst.test_client() as c:
        user = UserModel("ali", "majed", date(1991,3,26), "alimajed1991+5@gmail.com", "password123")
        user_dao.create_user(user)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        creds = {
            "email": "alimajed1991+5@gmail.com",
            "password": "password123"
        }
        req = c.post("http://localhost:5000/api/auth/", data=json.dumps(creds, default=json_serial), headers=headers)
        assert req.status_code == 200

        unauthorized_req = c.get("http://localhost:5000/api/home/protected")
        assert unauthorized_req.status_code == 401

        response = json.loads(req.data)
        access_token = response["access_token"]
        authorized_headers = {
            "Authorization": f"Bearer {access_token}"
        }
        authorized_req = c.get("http://localhost:5000/api/home/protected", headers=authorized_headers)
        assert authorized_req.status_code == 200

