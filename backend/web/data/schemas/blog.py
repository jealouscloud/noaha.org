import sqlalchemy
import sqlalchemy.dialects.sqlite as sqlite_dialect
from sqlalchemy.orm import declarative_base

from . import TZDateTime

Base = declarative_base()


class Posts(Base):
    __tablename__ = "posts"
    id = sqlalchemy.Column(sqlite_dialect.INTEGER(), primary_key=True)
    filepath = sqlalchemy.Column(sqlite_dialect.TEXT())
    title = sqlalchemy.Column(sqlite_dialect.TEXT())
    slug = sqlalchemy.Column(sqlite_dialect.TEXT())
    content = sqlalchemy.Column(sqlite_dialect.TEXT())
    created = sqlalchemy.Column(TZDateTime, nullable=False)
    last_edit = sqlalchemy.Column(TZDateTime, nullable=False)
    display = sqlalchemy.Column(sqlite_dialect.BOOLEAN(), default=True)
    # Unique constraints
    __table_args__ = (
        sqlalchemy.UniqueConstraint("title"),
        sqlalchemy.UniqueConstraint("filepath"),
        sqlalchemy.UniqueConstraint("slug"),
    )
