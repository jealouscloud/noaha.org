import html_compose as ht
from html_compose import (
    a,
    aside,
    body,
    h2,
    nav,
    p,
    section,
)

from .helpers import cache_bust


def header():
    return ht.header(id="header", class_="container-fluid")[
        section()[h2["Noah Ablaseau"], p[""]],
        nav(class_="navbar")[
            a(href="/")["demo"],
            a(href="/blog")["blog"],
            a(href="/about")["about"],
        ],
    ]


def main(*args, **kwargs):
    return ht.main(class_="container-fluid")[
        section(id="about")["Nothing is ever just something. "],
        section(id="content", class_=["content"])[kwargs.get("content", []),],
        aside(class_="sidebar")["Sidebar content like recent posts or links "],
    ]


def footer():
    return ht.footer(class_="container-fluid")["Contact info, copyright "]


def page(*args, **kwargs) -> body:
    return body()[header(), main(*args, **kwargs), footer()]


def fonts():
    return [
        ht.link(rel=["preconnect"], href="https://fonts.googleapis.com"),
        ht.link(
            rel=["preconnect"], href="https://fonts.gstatic.com", crossorigin=""
        ),
        ht.link(
            href="https://fonts.googleapis.com/css2?family=Ancizar+Sans:ital,wght@0,100..1000;1,100..1000&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap",
            rel=["stylesheet"],
        ),
    ]


def create(*args, **kwargs):
    doc = ht.HTML5Document(
        title="demo",
        head=[
            ht.script(src=cache_bust("/public/bundle.js")),
            ht.script(src=cache_bust("/public/vanillajs/index.js")),
            ht.link(rel="stylesheet", href=cache_bust("/public/css/main.css")),
            ht.link(
                rel="icon",
                href=cache_bust("/public/assets/favicon.ico"),
                type="image/x-icon",
            ),
            fonts(),
        ],
        body=page(*args, **kwargs),
    )
    return doc
