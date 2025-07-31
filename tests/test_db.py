from datetime import datetime

import backend.data.connectors.sqlite as sqlite_connector
from backend.data.adapters.users_adapter import (
    SqliteUsersAdapter as users_adapter,
)


def test_users():
    # No persistence
    sqlite_connector._resolve_path = lambda x: ":memory:"

    a = users_adapter()

    a.init()

    with a:
        a.add_user("John Doe", "test@example.com")
        u = a.get_user(1)
        assert u.email == "test@example.com"
        assert u.name == "John Doe"

    # Session tests
    with a:
        ses = a.login_user(1)
        now = datetime.now().astimezone()
        u = a.session_token_to_user(ses)
        last_login = a.get_user(1).last_login
        assert now > last_login, "Last login should be updated"

    with a:
        assert a.session_token_to_user("invalid_token") is None
