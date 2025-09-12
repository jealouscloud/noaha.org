from pathlib import Path

from flask import Flask

from . import hypertext
from .data import store

app = Flask(__name__, static_folder=Path("public").resolve())
store.init()


@app.route("/")
def hello_world():
    return hypertext.pages.home_page()


@app.route("/blog")
def blog_page():
    return hypertext.pages.blog_list_page(store.post_list())


@app.route("/about")
def about_page():
    return hypertext.pages.about_page()


@app.route("/guitar")
def guitar_page():
    return hypertext.pages.guitar()


@app.route("/blog/<slug>")
def blog_post(slug: str):
    post = store.blog_post(slug)
    if not post:
        return "Blog post not found", 404
    return hypertext.pages.blog_page(post)


app.debug = True
