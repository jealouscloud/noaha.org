import html_compose.elements as ht
from html_compose import unsafe_text

from ..markdown import read_markdown
from .helpers import cache_bust as cache_bust


def home():
    def br2():
        return ht.br(), ht.br()

    return ht.section[
        ht.article(class_="o-card")[
            ht.div["Welcome to the Hypertext World!"],
            ht.span[
                "I'm Noah, and this is ",
                ht.s["my favorite site on the citadel"],
                " my personal website.",
                br2(),
                "It's a bit of a work in progress. "
                "I'm trying to avoid frameworks while solving the problems that traditional frameworks solve. ",
                ht.br(),
                "To that end, this site is built with ",
                ht.a(href="https://github.com/jealouscloud/html-compose")[
                    "html-compose"
                ],
                ", a declarative way to build HTML from Python.",
            ],
        ]
    ]


def about():
    return ht.section(
        id="post-content",
        class_="content",
    )[
        ht.article(class_="o-card")[
            ht.h2()["About Me"],
            # horizontal split
            ht.hr(),
            unsafe_text(read_markdown("content/about.md").html_content),
        ],
    ]
