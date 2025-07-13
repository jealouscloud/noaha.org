import html_compose as ht

from .. import models
from ..markdown import read_markdown
from . import blog, common


def home():
    def br2():
        return ht.br(), ht.br()

    return common.create(
        content=ht.section[
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
    )


def blog_page(post: models.blog.Post):
    return common.create(content=blog.post(post))


def about_page():
    return common.create(
        content=ht.section(
            id="post-content",
            class_="content",
        )[
            ht.article(class_="o-card")[
                ht.h2()["About Me"],
                # horizontal split
                ht.hr(),
                ht.unsafe_text(read_markdown("content/about.md").html_content),
            ],
        ]
    )
