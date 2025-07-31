from datetime import datetime
from pathlib import Path
from typing import NamedTuple

from loguru import logger
from sqlalchemy import insert, select, update

from backend.markdown import read_markdown

from ..connectors.sqlite import SqliteConnector
from ..schemas import blog_schema
from . import param_check


class types:
    class post_description(NamedTuple):
        title: str
        slug: str
        created: datetime
        preview: str


class SqliteBlogPostsAdapter(SqliteConnector):
    def __init__(self, read_only: bool = False):
        super().__init__("blog_posts", mode="ro" if read_only else "rw")

    def init_schema(self) -> None:
        assert self.conn is None, "Database connection already established"
        with self:
            blog_schema.Base.metadata.create_all(self.engine)

    @staticmethod
    def init():
        adapter = SqliteBlogPostsAdapter(read_only=False)
        adapter.init_schema()
        with adapter:
            for file in Path("./content/blog/").glob("*.md"):
                logger.info(f"Syncing file {file}")
                adapter.sync_file(file)

    def get_posts(
        self, offset: int = 0, limit: int = 100
    ) -> list[types.post_description]:
        """
        Get all blog posts.
        :return: A list of blog posts.
        """
        post = blog_schema.Posts
        result = self.execute(
            select(post.title, post.slug, post.created, post.preview)
            .where(post.display)
            .order_by(post.id.desc())
            .order_by(post.created.desc())
            .offset(offset)
            .limit(limit)
        )
        param_check(result, types.post_description)
        return [types.post_description(*row) for row in result.fetchall()]

    def get_post_by_slug(self, slug: str):
        """
        Get a blog post by its slug.
        :param slug: The slug of the blog post.
        :return: The blog post if found, otherwise None.
        """
        assert self.conn, "Database connection not established"
        post = blog_schema.Posts
        result = self.execute(
            select(
                post.id, post.title, post.slug, post.content, post.created
            ).where(post.slug == slug)
        )
        data = result.one_or_none()
        if data is not None:

            class Post(NamedTuple):
                id: int
                title: str
                slug: str
                content: str
                created: datetime

            param_check(result, Post)
            return Post(*data)
        else:
            return None

    def sync_file(self, file_path: Path):
        """
        Sync a markdown file to the database.
        :param file_path: The path to the markdown file.
        """
        assert self.conn, "Database connection not established"

        class Post(NamedTuple):
            id: int
            last_edit: datetime

        now = datetime.now().astimezone()
        post = blog_schema.Posts
        result = self.execute(
            select(post.id, post.last_edit).where(
                post.filepath == str(file_path)
            )
        ).one_or_none()

        def md_data(want_id: bool = True) -> dict:
            """
            generate markdown content and metadata
            """
            md = read_markdown(file_path)
            id = md.frontmatter.get("id", None) if want_id else None
            return {
                "filepath": str(file_path),
                "slug": md.frontmatter.get("slug", file_path.stem),
                "title": md.frontmatter.get("title", file_path.stem),
                "display": md.frontmatter.get("display", True),
                "content": md.html_content,
                "preview": md.preview,
            } | (dict(id=id) if id is not None else {})

        s = file_path.stat()
        mdatetime = datetime.fromtimestamp(s.st_mtime).astimezone()

        if result is None:
            # post not found, we need to insert it

            md = read_markdown(file_path)
            created = md.frontmatter.get("post-date", None)
            if not created:
                created = now
            else:
                created = datetime.strptime(created, "%m-%d-%y").astimezone()

            mtime = int(file_path.stat().st_mtime)
            if mtime < created.timestamp():
                mdatetime = now

            want_id = True

            if (
                "id" in md.frontmatter
                and self.execute(
                    select(1).where(post.id == md.frontmatter.get("id"))
                ).one_or_none()
            ):
                # no conflicts, the md ids are a suggestion
                want_id = False

            self.execute(
                insert(post).values(
                    dict(last_edit=mdatetime, created=created)
                    | md_data(want_id=want_id)
                )
            )
            return

        rpost = Post(*result)

        if mdatetime > rpost.last_edit:
            self.execute(
                update(post)
                .where(post.id == rpost.id)
                .values(
                    dict(
                        last_edit=mdatetime,
                    )
                    | md_data(want_id=False)
                )
            )
        self.connection.commit()
