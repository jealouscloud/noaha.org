from flask import Flask

from . import hypertext

app = Flask(__name__, static_folder="../../public")


@app.route("/")
def hello_world():
    return hypertext.create()


app.debug = True
