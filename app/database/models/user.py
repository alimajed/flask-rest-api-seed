from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column
from sqlalchemy.types import DateTime, String
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from app.database.models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False, unique=True)

    def __init__(self, first_name, last_name, date_of_birth, email, plaintext_password):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.password = plaintext_password

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

    @hybrid_property
    def password(self):
        return self._password
 
    @password.setter
    def set_password(self, plaintext_password):
        self._password = generate_password_hash(plaintext_password)
 
    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return check_password_hash(self.password, plaintext_password)
