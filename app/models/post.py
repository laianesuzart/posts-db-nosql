from pymongo import MongoClient
from dotenv import dotenv_values
from datetime import datetime
from .exc import NonexistentPostError, InvalidDataError

config = dotenv_values('.env')
db_name = config['DB_NAME']

client = MongoClient('mongodb://localhost:27017/')

db = client[db_name]


class Post:
    POST_KEYS = {'title', 'author', 'tags', 'content'}

    def __init__(self, **kwargs):
        for key in self.POST_KEYS:
            if key not in kwargs:
                raise InvalidDataError(f'Key {key} not found.')
        self.has_only_valid_arguments(**kwargs)

        self.title = kwargs['title']
        self.author = kwargs['author']
        self.tags = kwargs['tags']
        self.content = kwargs['content']

    def get_id(self):
        try:
            posts_list = self.get_all()
            self.id = posts_list[-1]['id'] + 1
        except IndexError:
            self.id = 1

    def save(self):
        self.get_id()
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        db.posts.insert_one(self.__dict__)

        return db.posts.find_one({'id': self.id}, {'_id': False})

    @staticmethod
    def get_all():
        posts_list = list(db.posts.find({}, {'_id': False}))
        return posts_list

    @staticmethod
    def get_by_id(id: int):
        post = db.posts.find_one({'id': id}, {'_id': False})
        if not post:
            raise NonexistentPostError(id)
        return post

    @staticmethod
    def update(id: int, **kwargs):
        post = Post.get_by_id(id)
        Post.has_only_valid_arguments(**kwargs)
        for key in kwargs:
            post.update({key: kwargs[key]})
        post.update({'updated_at': datetime.utcnow()})
        db.posts.find_one_and_update({'id': id}, {'$set': post})

        return Post.get_by_id(id)

    @staticmethod
    def delete(id: int):
        deleted_post = db.posts.find_one_and_delete({'id': id}, {'_id': False})
        if not deleted_post:
            raise NonexistentPostError(id)
        return deleted_post
 
    @classmethod
    def has_only_valid_arguments(cls, **kwargs):
        for key in kwargs:
            if key not in cls.POST_KEYS:
                raise InvalidDataError(f'Key {key} not allowed.')
            if not type(kwargs[key]) == str and not key == 'tags':
                raise InvalidDataError(f'Key {key} should be a string.')
            if key == 'tags' and not type(kwargs[key]) == list:
                raise InvalidDataError(f'Key {key} should be a list of strings.')
