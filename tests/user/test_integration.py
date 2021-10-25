from datetime import date

from tests.config import app_inst
from app.database.models.user import UserModel
from app.daos.user import user_dao


def test_crud(app_inst):
    with app_inst.test_client() as c:
        user = UserModel("ali", "majed", date(1991,3,26), "alimajed1991+2@gmail.com", "password123")

        assert UserModel.find_by_email("alimajed1991+2@gmail.com") is None

        user_dao.create_user(user)

        assert UserModel.find_by_email("alimajed1991+2@gmail.com") is not None
        
        user_dao.delete_user(user)

        assert UserModel.find_by_email("alimajed1991+2@gmail.com") is None