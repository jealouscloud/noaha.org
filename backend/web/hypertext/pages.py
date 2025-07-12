import html_compose as ht

from .. import models
from . import blog, common


def home():
    return common.create(
        content=ht.section[
            ht.article(class_="o-card")[
                ht.div["Welcome to the Hypertext World!"],
                ht.span[
                    "I'm Noah Ablaseau, and this is my personal website.",
                    ht.br(),
                    ht.br(),
                ],
                ht.a(href="/blog")["Go to the Blog"],
            ]
        ]
    )


def blog_page(post: models.blog.Post):
    return common.create(content=blog.post(post))
