import sqlalchemy
import sqlalchemy.dialects.sqlite as sqlite_dialect
from sqlalchemy.orm import declarative_base

from . import TZDateTime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlite_dialect.INTEGER(), primary_key=True)
    name = sqlalchemy.Column(sqlite_dialect.TEXT())
    email = sqlalchemy.Column(sqlite_dialect.TEXT(), unique=True)
    last_login = sqlalchemy.Column(TZDateTime, nullable=True)


class Session(Base):
    __tablename__ = "sessions"
    id = sqlalchemy.Column(
        sqlite_dialect.INTEGER(), primary_key=True, autoincrement=True
    )
    user_id = sqlalchemy.Column(
        sqlite_dialect.INTEGER(), sqlalchemy.ForeignKey("users.id")
    )
    token_hash = sqlalchemy.Column(sqlite_dialect.TEXT(32), nullable=False)
    expiry = sqlalchemy.Column(TZDateTime)
