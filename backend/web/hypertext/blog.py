from html_compose import (
    a,
    article,
    div,
    h2,
    h4,
    hr,
    li,
    section,
    span,
    time,
    ul,
    unsafe_text,
)

from ..models import blog


def post(post: blog.Post):
    return section(
        id="post-content",
        class_="content",
    )[
        article(class_="o-card")[
            h2()[post.title],
            time[post.date.strftime("%m-%d-%Y")],
            # horizontal split
            hr(),
            unsafe_text(post.content),
        ],
    ]


def page_list(posts: list[blog.Post]):
    return section(id="post-list", class_="content")[
        section(class_="o-card")[
            ul(class_="o-post-list")[
                [
                    li()[
                        div(class_="post")[
                            h4()[a(href=f"/blog/{post.slug}")[post.title]],
                            hr(),
                            time[post.date.strftime("%b-%d-%Y")],
                        ],
                        span[
                            unsafe_text(post.preview)
                            if post.preview
                            else "No preview available"
                        ],
                    ]
                    # button()[a(href=f"/blog/{post.slug}")["Read more"]],
                    for post in posts
                ]
            ]
        ]
    ]
