from datetime import datetime
from typing import NamedTuple


class Post(NamedTuple):
    title: str
    slug: str
    content: str
    date: datetime
