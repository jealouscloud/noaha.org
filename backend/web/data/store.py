from contextlib import contextmanager

from ..models import blog
from .adapters import _sqlite


def init():
    """
    Any one-time run logic to happen per process/thread.
    """
    _sqlite.SqliteUsersAdapter.init()


def blog_post():
    return blog.Post(
        "My First Blog Post",
        "This is the content of my first blog post.",
        "2022-01-01",
    )


@contextmanager
def users(read_only=False):
    """
    Return a session with the users adapter.
    """
    adapter = _sqlite.SqliteUsersAdapter(read_only=read_only)
    with adapter:
        yield adapter
