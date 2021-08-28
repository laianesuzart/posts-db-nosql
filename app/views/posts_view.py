from flask import Flask, request
from ..models import Post
from ..services import save_post, get_all_posts


def posts_view(app: Flask):
    @app.post('/posts')
    def create_post():
        data = request.get_json()
        post = Post(**data)
        save_post(post)
        return {'msg': 'Post criado com sucesso'}, 201

    
    @app.get('/posts')
    def read_posts():
        return get_all_posts(), 200

    
    @app.get('/posts/<int:id>')
    def read_post_by_id(id: int):
        ...

    @app.patch('/posts/<int:id>')
    def update_post(id: int):
        ...
    
    @app.delete('/posts/<int:id>')
    def delete_post(id: int):
        ...
