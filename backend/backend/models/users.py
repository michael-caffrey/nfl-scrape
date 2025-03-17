from backend.models import db
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    model = db.Column(db.String(128), nullable=True)
    
    def __init__(self, username):
        self.username = username

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    @classmethod
    def by_username(cls, username):
        return cls.query.filter(cls.username == username).one_or_none()

