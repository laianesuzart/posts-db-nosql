from ..errors.posts import NonexistentPostError
from dataclasses import dataclass
from datetime import datetime
from ..services import db


@dataclass
class Post:
    title: str
    author: str
    tags: list
    content: str
    id: int = 1
    created_at: str = ''
    updated_at: str = ''

    @staticmethod
    def get_all_posts():
        posts_list = list(db.posts.find())
        [post.pop('_id') for post in posts_list]
        return posts_list

    @staticmethod
    def get_post_by_id(id):
        post = db.posts.find_one({'id': id})
        if not post:
            raise NonexistentPostError(id)
        post.pop('_id')
        return post

    def get_id(self):
        try:
            posts_list = self.get_all_posts()
            self.id = posts_list[-1]['id'] + 1
        except IndexError:
            ...

    def save_post(self):
        self.get_id()
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        db.posts.insert_one(self.__dict__)

    def update_post(self, **kwargs):
        for key in kwargs:
            self.key = kwargs[key]
        self.updated_at = datetime.utcnow()
