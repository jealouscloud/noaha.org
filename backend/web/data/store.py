from ..models import blog


def blog_post():
    return blog.Post(
        "My First Blog Post",
        "This is the content of my first blog post.",
        "2022-01-01",
    )


class Users:
    def __init__(self, adapter):
        self.adapter = adapter

    def session(self):
        pass
