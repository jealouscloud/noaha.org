from flask import Flask

from . import hypertext
from .data import store

app = Flask(__name__, static_folder="../../public")


@app.route("/")
def hello_world():
    return hypertext.pages.blog_page(store.blog_post())


app.debug = True
