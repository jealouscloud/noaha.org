"""
Centralized data access layer using the Adapter Pattern.

Decouples business logic from data backends, making it easy to switch
between different storage systems.

Put data transformation and business logic here - keep adapters simple
and focused purely on data access.

Good: store.get_user_posts(user_id), store.create_validated_post(data)
Avoid: store.get_adapter().query(...), exposing adapters to consumers
"""

from pathlib import Path

from ..models import blog
from .adapters.blog_adapter import SqliteBlogPostsAdapter
from .adapters.users import SqliteUsersAdapter


def init():
    """
    Any one-time run logic to happen per process/thread.
    """
    SqliteUsersAdapter.init()
    SqliteBlogPostsAdapter.init()


def blog_post(slug: str):
    adapter = SqliteBlogPostsAdapter()
    with adapter:
        result = adapter.get_post_by_slug(slug)
        if result:
            return blog.Post(
                title=result.title,
                slug=result.slug,
                content=result.content,
                date=result.created,
            )
    return None


def post_list(offset: int = 0, limit: int = 100):
    adapter = SqliteBlogPostsAdapter()
    postlist = []
    with adapter:
        result = adapter.get_posts(offset, limit)
        for row in result:
            postlist.append(
                blog.Post(
                    title=row.title,
                    slug=row.slug,
                    content="",
                    date=row.created,
                    preview=row.preview,
                )
            )
    return postlist


def sync_file(filename: Path):
    adapter = SqliteBlogPostsAdapter()
    with adapter:
        adapter.sync_file(filename)
