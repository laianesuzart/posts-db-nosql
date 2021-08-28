from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar


@dataclass
class Post:
    title: str
    author: str
    tags: list
    content: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    last_id: ClassVar[int] = [1]
    post_id: int = last_id[-1]

    def update_post(self, **kwargs):
        for key in kwargs:
            self.key = kwargs[key]
        self.updated_at = datetime.utcnow()
    
    @classmethod
    def update_last_id(cls):
        cls.last_id.append(cls.last_id[-1] + 1)
