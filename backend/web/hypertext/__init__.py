import html_compose as ht
from html_compose import (
    article,
    aside,
    body,
    button,
    footer,
    h2,
    header,
    main,
    nav,
    p,
    section,
)

from .helpers import cache_bust


def page():
    b = body()
    b.append(
        header(id="header")[
            section(id="hero")[h2["My Blog"], p["Demo of demos"]],
            nav()["Navigation links "],
        ]
    )
    b.append(
        main()[
            section(id="about")["About section or summary "],
            section(id="blog")[
                article()[
                    h2()["Blog Post Title"],
                    p()["Post content..."],
                    button["Demo button"],
                ],
                "Repeat <article> for each post ",
            ],
            aside()["Sidebar content like recent posts or links "],
        ]
    )
    b.append(footer()["Contact info, copyright "])

    return b


footer()["Contact info, copyright "]


def create():
    body = page()
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
        body=body,
    )
    return doc


def display() -> int:
    print(create())


#
