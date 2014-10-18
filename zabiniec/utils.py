# -*- coding: utf-8 -*-
import os


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
