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
    """Buduje absolutą biorąc folder projektu jako root

    :param path: ścieżka do jakie pliku w projekcie
    :returns: absolutą ścieżkę
    :rtype: str

    """
    return os.path.join(PROJECT_ROOT, path)


def app_runner(app, prod=False):
    """Funkcja uruchamiająca aplikację

    :param app: aplikacja flask
    :param prod: czy uruchamiamy produkcyjnie

    """
    if prod:
        raise NotADirectoryError('Dopisze jak zdąrze')
    else:
        app.run()


# no i to jest dekorator, czyli takie coś co dekoruje funkcje,
# czyli zmienia jej właściwości, trochę trudne to i wyjaśni
# Troll Żabce jak już wszystko inne złapie:*
# dla ambitnych Żab:
# http://pythonista.net/blog/2010/dekoratory1/
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
