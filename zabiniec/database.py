# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

from flask import g


def _load_data(db):
    """Ląduje dane początkowe do aplikacji

    :param db: baza danych
    """
    from .models import User, App
    try:
        App.get(App.initialized == True)
    except App.DoesNotExist:
        print('Ładuje Żapkę i Marnego Trola..')
        with db.transaction():
            app = App(initialized=True)
            app.save()
            troll = User(
                username=User.TROLL,
                question='Ulubione Żabie święto?',
                answer='Żabanuka'
            )
            troll.save()
            zabka = User(
                username=User.ZABKA,
                question='Jak Marny Troll niegrzeczny to go..?',
                answer='wałkiem'
            )
            zabka.save()


def create_db(app):
    db_params = {}
    if app.config.get('DB_USER'):
        db_params['user'] = app.config['DB_USER']
    if app.config.get('DB_HOST'):
        db_params['host'] = app.config['DB_HOST']
    if app.config.get('DB_PORT'):
        db_params['port'] = app.config['DB_PORT']
    if app.config.get('DB_PASSWORD'):
        db_params['password'] = app.config['DB_PASSWORD']
    db = app.config['DB_CLASS'](app.config['DB_NAME'])
    # bazę danych zawsze przechowuje w zmiennej globalnej,
    # aby to działało trzeba wszystko uruchomić w kontekście aplikacji flask
    # dlatego to dziwactwo w run.py
    g.db = db
    db.connect()
    # importuje modele i tworze tabele do przechowywania danych dla nich
    from .models import User, List, ListField, App
    db.create_tables([User, List, ListField, App], safe=True)
    _load_data(db)


# Nie lubimy używać bezpośrednio zmiennych globalnych dlatego ten fakt
# chowamy pod funkcją.
def get_db():
    """Pobiera objekt bazy danych

    :returns: Baza danych
    :rtype: peewee.Database

    """
    return g.db
