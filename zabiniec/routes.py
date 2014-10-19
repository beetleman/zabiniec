# -*- coding: utf-8 -*-
from .views import (
    index,
    login,
    lists,
    logout,
)


def create_routes(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login', 'login', login,  methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/lists', 'lists', lists)

