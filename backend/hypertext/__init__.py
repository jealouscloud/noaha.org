import html_compose.elements as e
from html_compose import HTML5Document

from .helpers import cache_bust


def create(*args, **kwargs):
    """
    Create a complete HTML document with the given content and other parameters.
    """
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
            common.fonts(),
        ],
        body=common.page(*args, **kwargs),
    )
    return doc


from . import blog, common, pages  # noqa: E402

__all__ = ["common", "pages", "blog", "cache_bust", "create"]
