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
    delete_listfield,
    view_list,
    toggle_listfield,
)


def create_routes(app):
    # tworzy połączenia między funkcjami z views.py
    # a adresami które wpisywane są w przeglądarce

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login', 'login', login,  methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/lists', 'lists', lists)
    # omiwie to na tym przykładzie:
    app.add_url_rule(
        '/change_passwd',  # adres
        'change_passwd',  # skutkować nazwa po której można się
                          # odwoływać do adresu
        change_passwd,  # widok który zostanie wywołany
        methods=['GET', 'POST']  # dozwolone metody
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
    app.add_url_rule(
        '/delete_listfield/<int:list_id>/<int:field_id>',
        'delete_listfield',
        delete_listfield,
    )
    app.add_url_rule(
        '/view_list/<int:list_id>',
        'view_list',
        view_list
    )
    app.add_url_rule(
        '/toggle_listfield/<int:list_id>/<int:field_id>',
        'toggle_listfield',
        toggle_listfield,
    )
