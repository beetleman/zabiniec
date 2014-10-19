# -*- coding: utf-8 -*-
from flask import g


def _load_data(db):
    from .models import User, App
    try:
        App.get(App.initialized == True)
    except App.DoesNotExist:
        print('Ładuje Żapkę i Marnego Trola..')
        with db.transaction():
            app = App(initialized=True)
            app.save()
            troll = User(
                username='troll',
                question='Ulubione Żabie święto?',
                answer='Żabanuka'
            )
            troll.save()
            zabka = User(
                username='zabka',
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
    g.db = db
    db.connect()
    from .models import User, List, ListField, App
    db.create_tables([User, List, ListField, App], safe=True)
    _load_data(db)


def get_db():
    return g.db
