from datetime import datetime

import sqlalchemy.dialects.sqlite as sqlite_dialect
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import String, TypeDecorator


class TZDateTime(TypeDecorator):
    """
    This is a custom SQLAlchemy type for storing timezone-aware datetimes
    in SQLite.
    It ensures that the datetime is stored in ISO 8601 format
    """

    impl = String
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            if value.tzinfo is None:
                raise ValueError("Naive datetimes not allowed!")
            # Use full ISO format with offset
            return value.isoformat()
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            # This will parse offset-aware ISO strings
            return datetime.fromisoformat(value)
        return value
