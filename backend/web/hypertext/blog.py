from html_compose import article, button, h2, section, time

from ..models import blog


def post(post: blog.Post):
    return section(id="post-content")[
        article(class_="o-card")[
            h2()[post.title],
            time[post.date],
            post.content,
            button["Demo button"],
        ],
    ]
