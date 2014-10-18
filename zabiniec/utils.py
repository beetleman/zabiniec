# -*- coding: utf-8 -*-
import os
from functools import wraps
from flask import g

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
        g.current_object = func
        return func(*args, **kwargs)
    return f
