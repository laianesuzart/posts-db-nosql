from flask import Flask


def init_app(app: Flask):
    from .posts_view import posts_view
    posts_view(app)

    return app
