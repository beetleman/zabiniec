# -*- coding: utf-8 -*-

from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    with app.app_context():
        from .context_processors import register_context_processors
        register_context_processors(app)
        from .templatetags import register_templatetags
        register_templatetags(app)
        from .database import create_db
        create_db(app)
        from .routes import create_routes
        create_routes(app)
    return app
