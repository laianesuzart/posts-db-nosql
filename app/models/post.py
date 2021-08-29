from dataclasses import dataclass
from datetime import datetime
from ..services import db
from .exc import NonexistentPostError, InvalidDataError

POST_KEYS = {'title', 'author', 'tags', 'content'}


@dataclass
class Post:
    title: str
    author: str
    tags: list
    content: str
    id: int = 1
    created_at: str = ''
    updated_at: str = ''

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

    @staticmethod
    def get_all_posts():
        posts_list = list(db.posts.find())
        [post.pop('_id') for post in posts_list]
        return posts_list

    @staticmethod
    def get_post_by_id(id: int):
        post = db.posts.find_one({'id': id})
        if not post:
            raise NonexistentPostError(id)
        post.pop('_id')
        return post
    
    @staticmethod
    def update_post(old_post: dict, **kwargs):
        for key in kwargs:
            old_post.update({key: kwargs[key]})
        old_post.update({'updated_at': datetime.utcnow()})
        db.posts.find_one_and_update({'id': old_post['id']}, {'$set': old_post})

    @staticmethod
    def delete_post(id: int):
        deleted_post = db.posts.find_one_and_delete({'id': id})
        if not deleted_post:
            raise NonexistentPostError(id)
        deleted_post.pop('_id')
        return deleted_post

    @staticmethod
    def has_all_arguments(**kwargs):
        for key in POST_KEYS:
            if key not in kwargs:
                raise InvalidDataError(f'Key {key} not found.')

    @staticmethod
    def has_only_valid_arguments(**kwargs):
        for key in kwargs:
            if key not in POST_KEYS:
                raise InvalidDataError(f'Key {key} not allowed.')
            if not type(kwargs[key]) == str and not key == 'tags':
                raise InvalidDataError(f'Key {key} should be a string.')
            if key == 'tags' and not type(kwargs[key]) == list:
                raise InvalidDataError(f'Key {key} should be a list of strings.')
