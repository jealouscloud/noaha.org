from datetime import datetime, timedelta

import sqlalchemy
import sqlite_utils


def test_users():
    import web.data.adapters._sqlite as sqlite_adapter

    # No persistence
    sqlite_adapter._resolve_path = lambda x: ":memory:"

    a = sqlite_adapter.SqliteUsersAdapter()

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
        assert last_login > now
    assert False
