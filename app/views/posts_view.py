from flask import Flask, request, jsonify
from ..models import Post
from ..errors.posts import NonexistentPostError


def posts_view(app: Flask):
    @app.post('/posts')
    def create_post():
        data = request.get_json()
        post = Post(**data)
        post.save_post()
        return {'msg': 'Successful created post.'}, 201

    
    @app.get('/posts')
    def read_posts():
        posts_list = Post.get_all_posts()
        return jsonify(posts_list), 200

    
    @app.get('/posts/<int:id>')
    def read_post_by_id(id: int):
        try:
            return Post.get_post_by_id(id), 200
        except NonexistentPostError as err:
            return err.message, 404

    @app.patch('/posts/<int:id>')
    def update_post(id: int):
        ...
    
    @app.delete('/posts/<int:id>')
    def delete_post(id: int):
        ...
