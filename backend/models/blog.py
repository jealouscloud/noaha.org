from datetime import datetime
from typing import NamedTuple, Optional


class Post(NamedTuple):
    title: str
    slug: str
    content: str
    date: datetime
    preview: Optional[str] = None
