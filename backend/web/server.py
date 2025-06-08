from flask import Flask

from . import hypertext
from .data import store

app = Flask(__name__, static_folder="../../public")
store.init()


@app.route("/")
def hello_world():
    return hypertext.pages.home()


@app.route("/blog")
def blog_page():
    return hypertext.common.create(
        content=hypertext.blog.page_list(store.post_list())
    )


@app.route("/blog/<slug>")
def blog_post(slug: str):
    post = store.blog_post(slug)
    if not post:
        return "Blog post not found", 404
    return hypertext.common.create(content=hypertext.blog.post(post))


app.debug = True
