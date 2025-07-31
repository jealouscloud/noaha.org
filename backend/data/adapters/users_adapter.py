import secrets
from datetime import datetime, timedelta
from hashlib import md5
from typing import NamedTuple

from sqlalchemy import insert, select, update

from ..connectors.sqlite import SqliteConnector
from ..schemas import users_schema


class types:
    class get_user_result(NamedTuple):
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
            users_schema.Base.metadata.create_all(self.engine)

    @staticmethod
    def init():
        adapter = SqliteUsersAdapter(read_only=False)
        adapter.init_schema()

    # region session management
    def session_token_to_user(
        self, session_token: str
    ) -> None | types.get_user_result:
        """
        Get the user associated with a session token.
        :param session_token: The session token to look up.
        :return: The user associated with the session token, or None if not found / expired.
        """
        conn = self.connection
        now = datetime.now().astimezone()
        session = users_schema.Session
        result = conn.execute(
            select(session.user_id, session.expiry).where(
                session.expiry > now,
                session.token_hash
                == md5(session_token.encode("utf-8")).hexdigest(),
            )
        )

        data = result.fetchone()
        if data is None:
            return None

        user_id, expiry = data
        assert expiry > now, "Session token expired but database returned it"

        try:
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

        now = datetime.now().astimezone()
        user = users_schema.User
        session = users_schema.Session

        self.execute(
            update(user).where(user.id == user_id).values(last_login=now)
        )

        self.execute(
            insert(session).values(
                user_id=user_id,
                expiry=now + timedelta(hours=1),
                token_hash=token_hash,
            )
        )

        self.connection.commit()
        return token

    # endregion

    # region user management
    def add_user(self, user: str, email: str):
        assert self.conn, "Database connection not established"
        self.conn.execute(
            insert(users_schema.User).values(
                name=user, email=email, last_login=datetime.now().astimezone()
            )
        )

    def get_user(self, user_id: int) -> types.get_user_result:
        assert self.conn, "Database connection not established"
        result = self.conn.execute(
            select(
                users_schema.User.id,
                users_schema.User.name,
                users_schema.User.email,
                users_schema.User.last_login,
            ).where(users_schema.User.id == user_id)
        )
        data = result.fetchone()
        if data is None:
            raise ValueError(f"User with id {user_id} not found")

        return types.get_user_result(*data)

    # endregion
