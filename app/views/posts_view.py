from flask import Flask, request
from flask.json import jsonify
from ..models import Post


def posts_view(app: Flask):
    @app.post('/posts')
    def create_post():
        data = request.get_json()
        post = Post(**data)
        post.save_post()
        return {'msg': 'Post criado com sucesso'}, 201

    
    @app.get('/posts')
    def read_posts():
        posts_list = Post.get_all_posts()
        return jsonify(posts_list), 200

    
    @app.get('/posts/<int:id>')
    def read_post_by_id(id: int):
        ...

    @app.patch('/posts/<int:id>')
    def update_post(id: int):
        ...
    
    @app.delete('/posts/<int:id>')
    def delete_post(id: int):
        ...
