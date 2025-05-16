from . import hypertext


def main() -> int:
    from . import markdown

    print(markdown.read_markdown("content/blog/semantics.md"))
    return 0
