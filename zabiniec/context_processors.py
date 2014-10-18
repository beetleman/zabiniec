# -*- coding: utf-8 -*-
from inspect import getsource

from flask import g


def get_source_code():
    source_code = None
    if hasattr(g, 'current_object'):
        source_code = getsource(g.current_object)
    return {'source_code': source_code}


def register_context_processors(app):
    app.context_processor(get_source_code)
