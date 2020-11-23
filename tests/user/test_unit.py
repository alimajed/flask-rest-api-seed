from datetime import date

from app.database.models.user import UserModel


def test_create_user():
    user = UserModel("ali", "majed", date(1991,3,26), "alimajed1991+1@gmail.com", "password123")

    assert user.first_name == "ali"
    assert user.last_name == "majed"
    assert user.date_of_birth == date(1991,3,26)
    assert user.email == "alimajed1991+1@gmail.com"
    assert user.is_correct_password("password123") == True