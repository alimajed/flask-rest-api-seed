from pytz import timezone
from datetime import datetime
from uuid import uuid4

from flask import abort
from sqlalchemy import Column
from sqlalchemy.types import Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import SQLAlchemyError

from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone("UTC")))
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        if self.created_at:
            self.updated_at = datetime.now(timezone("UTC"))
        # handle sqlalchemy integrity error / psycopg2 error
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, e.__dict__['orig'])

    def delete_from_db(self) -> None:
        # handle sqlalchemy integrity error / psycopg2 error
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, e.__dict__['orig'])