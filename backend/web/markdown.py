from collections import namedtuple

import mistletoe
import yaml
from html_compose import unsafe_text

Markdown = namedtuple("Markdown", ["frontmatter", "html_content"])


def read_markdown(file_path):
    with open(file_path, "r") as f:
        md_content = f.read()
    md_start = 0
    frontmatter = {}
    END_FRONTMATTER = "\n---\n"
    if md_content.startswith("---"):
        try:
            fm_end = md_content.index(END_FRONTMATTER)
        except ValueError:
            raise ValueError(
                f"Invalid frontmatter in Markdown file {file_path}"
            )
        md_start = fm_end + len(END_FRONTMATTER)
        frontmatter = yaml.load(md_content[:fm_end], yaml.CSafeLoader)

    html_content = mistletoe.markdown(md_content[md_start:])
    return Markdown(
        frontmatter=frontmatter, html_content=unsafe_text(html_content)
    )
