# -*- coding: utf-8 -*-
from .views import (
    index,
    login,
    lists,
    logout,
    change_passwd,
)


def create_routes(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login', 'login', login,  methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/lists', 'lists', lists)
    app.add_url_rule(
        '/change_passwd',
        'change_passwd',
        change_passwd,
        methods=['GET', 'POST']
    )
