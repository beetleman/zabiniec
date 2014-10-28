# -*- coding: utf-8 -*-
import os
import uuid
import json
from functools import wraps
from inspect import getsource, getfile

from simplekv.fs import FilesystemStore
from flask import session

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
        porn = session.get('porn', [])
        title = getfile(func).replace(PROJECT_ROOT, 'zabiniec')
        porn.append({
            'title': title,
            'content': getsource(func)
        })
        session['porn'] = porn
        session.modified = True
        return func(*args, **kwargs)
    return f
