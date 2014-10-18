# -*- coding: utf-8 -*-
from .views import (
    index,
)


def create_routes(app):
    app.add_url_rule('/', 'index', index)
