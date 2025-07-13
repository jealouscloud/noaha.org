from datetime import datetime
from functools import cache

import html_compose.elements as e
from html_compose import HTML5Document, a, aside, body, div, h2, nav, p, section

from .helpers import cache_bust


def header():
    return e.header(id="header", class_="container-fluid o-header")[
        [
            div[
                h2(class_="title")[a(href="/")["Noah Ablaseau"]],
                p(class_="subheading")["Nothing is ever just something. "],
            ],
        ],
        nav(class_=["navbar"])[
            a(href="/blog")["blog"],
            a(href="/about")["about"],
        ],
    ]


def main(*args, **kwargs):
    return e.main(class_="container-fluid")[
        section(id="content", class_=["content"])[kwargs.get("content", []),],
        # aside(class_="sidebar")["Sidebar content like recent posts or links "],
    ]


@cache
def footer():
    return e.footer(class_="container-fluid")[
        f"©{datetime.now().year} Noah Ablaseau"
    ]


def page(*args, **kwargs) -> body:
    return body()[header(), main(*args, **kwargs), footer()]


def fonts():
    return [
        e.link(rel=["preconnect"], href="https://fonts.googleapis.com"),
        e.link(
            rel=["preconnect"], href="https://fonts.gstatic.com", crossorigin=""
        ),
        e.link(
            href="https://fonts.googleapis.com/css2?family=Ancizar+Sans:ital,wght@0,100..1000;1,100..1000&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap",
            rel=["stylesheet"],
        ),
    ]


def create(*args, **kwargs):
    doc = HTML5Document(
        title="Noah Ablaseau",
        head=[
            e.script(src=cache_bust("/public/bundle.js")),
            e.script(src=cache_bust("/public/vanillajs/index.js")),
            e.link(rel="stylesheet", href=cache_bust("/public/css/main.css")),
            e.link(
                rel="icon",
                href=cache_bust("/public/assets/favicon.ico"),
                type="image/x-icon",
            ),
            fonts(),
        ],
        body=page(*args, **kwargs),
    )
    return doc
