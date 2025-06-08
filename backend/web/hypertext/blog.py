from html_compose import (
    a,
    article,
    button,
    h2,
    section,
    span,
    time,
    unsafe_text,
)

from ..models import blog


def post(post: blog.Post):
    return section(id="post-content", class_="content")[
        article(class_="o-card")[
            h2()[post.title],
            time[post.date.strftime("%m-%d-%Y")],
            unsafe_text(post.content),
            button["Demo button"],
        ],
    ]


def page_list(posts: list[blog.Post]):
    return section(id="post-list", class_="content")[
        section(class_="o-card")[
            (
                (
                    span[
                        h2()[post.title],
                        time[post.date.strftime("%m-%d-%Y")],
                    ],
                    span[
                        unsafe_text(post.preview or "No preview available"),
                        "...",
                    ],
                    button()[a(href=f"/blog/{post.slug}")["Read more"]],
                )
                for post in posts
            ),
        ]
    ]
