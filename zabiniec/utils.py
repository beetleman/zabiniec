# -*- coding: utf-8 -*-
import os
import uuid
from functools import wraps

from flask import g, session

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)


def get_abspath(path):
    return os.path.join(PROJECT_ROOT, path)


def app_runner(app, prod=False):
    if prod:
        raise NotADirectoryError('Dopisze jak zdąrze')
    else:
        app.run()


def porn(func):
    @wraps(func)
    def f(*args, **kwargs):
        if not hasattr(g, 'porn'):
            g.porn = {}
        if 'porn_key' not in session:
            porn_key = uuid.uuid1().bytes
            session['porn_key'] = porn_key
            session.modified = True
        else:
            porn_key = session['porn_key']
        porn = g.porn.get(porn_key, [])
        porn.append(func)
        g.porn[porn_key] = porn
        return func(*args, **kwargs)
    return f
