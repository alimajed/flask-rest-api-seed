from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column
from sqlalchemy.types import Date, String

from app.database.models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(300), nullable=False)

    def __init__(self, first_name, last_name, date_of_birth, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

    def is_correct_password(self, plaintext_password):
        return check_password_hash(self.password, plaintext_password)

    @classmethod
    def find_by_email(cls, email: str):
        return cls.query.filter_by(email=email).first()

