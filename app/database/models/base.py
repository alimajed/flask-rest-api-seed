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