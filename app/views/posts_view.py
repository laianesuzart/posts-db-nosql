from flask import Flask, request, jsonify
from ..models import Post, NonexistentPostError, InvalidDataError


def posts_view(app: Flask):
    @app.post('/posts')
    def create_post():
        try:
            data = request.get_json()
            post = Post(**data)
            new_post = post.save()
            return new_post, 201
        except InvalidDataError as err:
            return err.message, 400

    @app.get('/posts')
    def read_posts():
        posts_list = Post.get_all()
        return jsonify(posts_list), 200

    @app.get('/posts/<int:id>')
    def read_post_by_id(id: int):
        try:
            post = Post.get_by_id(id)
            return post, 200
        except NonexistentPostError as err:
            return err.message, 404

    @app.patch('/posts/<int:id>')
    def update_post(id: int):
        try:
            data = request.get_json()
            post = Post.update(id, **data)
            return post, 200
        except NonexistentPostError as err:
            return err.message, 404
        except InvalidDataError as err:
            return err.message, 400

    @app.delete('/posts/<int:id>')
    def delete_post(id: int):
        try: 
           deleted_post = Post.delete(id)
           return deleted_post, 200
        except NonexistentPostError as err:
            return err.message, 404
