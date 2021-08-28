from flask.json import jsonify
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['kenzie']


def save_post(post):
    return db.posts.insert_one(post.__dict__)


def get_all_posts():
    database = list(db.posts.find())
    [post.pop('_id') for post in database]
    return jsonify(database)
