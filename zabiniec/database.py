# -*- coding: utf-8 -*-
from flask import g


def create_db(app):
    db_params = {}
    if  app.config.get('DB_USER'):
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
    from .models import User
    db.create_tables([User], safe=True)


def get_db():
    return g.db
