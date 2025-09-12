"""
In this file we return full HTML documents based on input parameters.

"""

from .. import models
from . import blog, create, home


def home_page():
    return create(content=home.home())


def blog_page(post: models.blog.Post):
    return create(content=blog.post(post))


def blog_list_page(posts: list[models.blog.Post]):
    return create(content=blog.page_list(posts))


def about_page():
    return create(content=home.about())


def guitar():
    return create(content=home.frets())
