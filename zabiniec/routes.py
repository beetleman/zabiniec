# -*- coding: utf-8 -*-
from .views import (
    index,
    login,
    lists,
    logout,
    change_passwd,
    edit_list,
    add_list,
    delete_list,
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
    app.add_url_rule(
        '/edit_list/<int:list_id>',
        'edit_list',
        edit_list,
        methods=['GET', 'POST']
    )
    app.add_url_rule(
        '/add_list',
        'add_list',
        add_list,
        methods=['GET', 'POST']
    )
    app.add_url_rule(
        '/delete_list/<int:list_id>',
        'delete_list',
        delete_list,
    )
