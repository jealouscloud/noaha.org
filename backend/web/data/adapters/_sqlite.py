"""
SQLite database adapters
The adapter pattern is used to provide a consistent interface
for different database backends.
"""

import secrets
from datetime import datetime, timezone
from hashlib import md5
from pathlib import Path
from typing import Literal, NamedTuple, Optional

import sqlalchemy
import sqlalchemy.dialects.sqlite as sqlite_dialect
from flask import sessions
from sqlalchemy import ForeignKey, Table, text
from sqlalchemy.engine import Connection

CONNECTORS = {}


def _resolve_path(title) -> Path:
    data = Path("./data")
    if not data.exists():
        data.mkdir()

    return data / f"{title}.db"


def _now():
    return datetime.now(timezone.utc).timestamp()


class SqliteConnector:
    """
    A connection to a SQLite database.
    """

    ENGINES = {}

    def __init__(
        self, path, mode: Literal["ro", "rw", "rwc"] = "rw", timeout=5
    ):
        self.path = _resolve_path(path)

        # hold the open conn if we have one
        self.conn: Optional[Connection] = None
        if mode == "rw":
            mode = "rwc"

        self.mode = mode
        self.timeout = timeout

    @property
    def connection(self) -> Connection:
        """
        Get the connection to the SQLite database.
        """
        if self.conn is None:
            raise RuntimeError("Database connection not established")
        return self.conn

    def connect_string(self) -> str:
        return f"{self.path}?mode={self.mode}&timeout={self.timeout}"

    def __enter__(self):
        """Establish a connection to the SQLite database and start transaction"""
        if self.conn:
            raise RuntimeError(
                "Database connection already established, use __exit__ to close it"
            )

        uri = f"{self.path}:{self.mode}"
        if uri in CONNECTORS:
            engine = CONNECTORS[uri]
        else:
            engine = sqlalchemy.create_engine(
                f"sqlite:///{self.connect_string()}"
            )
            CONNECTORS[uri] = engine
        conn = engine.connect()
        self.conn = conn
        # conn.__enter__()  # start transaction
        # WAL generally more efficient for concurrent reads/writes
        conn.execute(text("PRAGMA journal_mode=WAL"))
        # Enable foreign key constraints
        conn.execute(text("PRAGMA foreign_keys=ON"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None and exc_val is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.__exit__(exc_type, exc_val, exc_tb)
            self.conn.close()
            self.conn = None


class types:
    class user_result(NamedTuple):
        id: int
        name: str
        email: str
        last_login: datetime


class SqliteUsersAdapter(SqliteConnector):
    # class User(sqlmodel):
    def __init__(self, read_only: bool = False):
        super().__init__("users", mode="ro" if read_only else "rw")

    def init_schema(self) -> None:
        assert self.conn is None, "Database connection already established"
        with self:
            md = sqlalchemy.MetaData()
            Table(
                "users",
                md,
                sqlalchemy.Column(
                    "id", sqlite_dialect.INTEGER(), primary_key=True
                ),
                sqlalchemy.Column("name", sqlite_dialect.TEXT()),
                sqlalchemy.Column("email", sqlite_dialect.TEXT()),
                sqlalchemy.Column(
                    "last_login", sqlite_dialect.TIMESTAMP(), nullable=True
                ),
                sqlalchemy.UniqueConstraint("email"),
            )
            Table(
                "sessions",
                md,
                sqlalchemy.Column(
                    "id",
                    sqlite_dialect.INTEGER(),
                    primary_key=True,
                    autoincrement=True,
                ),
                sqlalchemy.Column(
                    "user_id", sqlite_dialect.INTEGER(), ForeignKey("users.id")
                ),
                sqlalchemy.Column(
                    "token_hash", sqlite_dialect.TEXT(32), nullable=False
                ),
                sqlalchemy.Column("expiry", sqlite_dialect.TIMESTAMP()),
            )
            md.create_all(self.connection)

    @staticmethod
    def init():
        adapter = SqliteUsersAdapter(read_only=False)
        adapter.init_schema()

    # region session management
    def session_token_to_user(
        self, session_token: str
    ) -> None | types.user_result:
        """
        Get the user associated with a session token.
        :param session_token: The session token to look up.
        :return: The user associated with the session token, or None if not found / expired.
        """
        assert self.conn, "Database connection not established"
        now = _now()
        result = self.conn.execute(
            text(
                "SELECT user_id, expiry FROM sessions WHERE expiry > :now AND token_hash = :token_hash"
            ),
            {
                "now": now,
                "token_hash": md5(session_token.encode("utf-8")).hexdigest(),
            },
        )

        data = result.fetchone()
        if data is None:
            return None

        user_id, expiry = data
        assert expiry > now, "Session token expired but database returned it"

        try:
            self.conn.execute(
                text(
                    "UPDATE users SET last_login = :last_login WHERE id = :id"
                ),
                {
                    "last_login": now,
                    "id": user_id,
                },
            )
            user = self.get_user(user_id)
            return user
        except ValueError:
            return None

    def login_user(self, user_id: int) -> str:
        """
        Log in a user and create a session token.
        :param user_id: The ID of the user to log in.
        :return: The session token.
        """
        assert self.conn, "Database connection not established"
        token = secrets.token_urlsafe(32)
        token_hash = md5(token.encode("utf-8")).hexdigest()

        now = datetime.now(timezone.utc).timestamp()
        self.conn.execute(
            text("UPDATE users SET last_login = :last_login WHERE id = :id"),
            {
                "last_login": now,
                "id": user_id,
            },
        )

        self.conn.execute(
            text(
                "INSERT INTO sessions (user_id, expiry, token_hash) "
                "VALUES (:user_id, :expiry, :token_hash)"
            ),
            {
                "user_id": user_id,
                "expiry": now + 3600,
                "token_hash": token_hash,
            },
        )
        return token

    # endregion

    # region user management
    def add_user(self, user: str, email: str):
        assert self.conn, "Database connection not established"
        self.conn.execute(
            text(
                "INSERT INTO users (name, email, last_login) VALUES (:name, :email, :last_login)"
            ),
            {
                "name": user,
                "email": email,
                "last_login": datetime.now(timezone.utc).timestamp(),
            },
        )

    def get_user(self, user_id: int) -> types.user_result:
        assert self.conn, "Database connection not established"
        result = self.conn.execute(
            text("SELECT * FROM users WHERE id = :id"), {"id": user_id}
        )

        data = result.fetchone()
        if data is None:
            raise ValueError(f"User with id {user_id} not found")

        return types.user_result(
            id=data[0],
            name=data[1],
            email=data[2],
            last_login=datetime.fromtimestamp(data[3], timezone.utc),
        )

    # endregion
