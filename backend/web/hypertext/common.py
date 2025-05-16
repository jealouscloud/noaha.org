import html_compose as ht
from html_compose import (
    aside,
    body,
    h2,
    nav,
    p,
    section,
)

from .helpers import cache_bust


def header():
    return ht.header(id="header")[
        section()[h2["Noah Ablaseau"], p[""]],
        nav()["Navigation links "],
    ]


def main(*args, **kwargs):
    return ht.main()[
        section(id="about")["About section or summary "],
        section(id="content")[kwargs.get("content", []),],
        aside()["Sidebar content like recent posts or links "],
    ]


def footer():
    return ht.footer()["Contact info, copyright "]


def page(*args, **kwargs) -> body:
    return body()[header(), main(*args, **kwargs), footer()]


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
        ],
        body=page(*args, **kwargs),
    )
    return doc
