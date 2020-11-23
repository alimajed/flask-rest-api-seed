from datetime import date

from tests.config import app_inst
from app.database.models.user import UserModel


def test_crud(app_inst):
    with app_inst.test_client() as c:
        user = UserModel("ali", "majed", date(1991,3,26), "alimajed1991+2@gmail.com", "password123")

        assert UserModel.find_by_email("alimajed1991+2@gmail.com") is None

        user.save_to_db()

        assert UserModel.find_by_email("alimajed1991+2@gmail.com") is not None
        
        user.delete_from_db()

        assert UserModel.find_by_email("alimajed1991+2@gmail.com") is None