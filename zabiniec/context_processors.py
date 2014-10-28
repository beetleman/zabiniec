# -*- coding: utf-8 -*-
from inspect import getsource, getfile
from flask import session

from .utils import PROJECT_ROOT, porn


@porn
def get_source_code():
    porn = session.get('porn', [])
    session['porn'] = []
    return {'source_code': porn}


def register_context_processors(app):
    app.context_processor(get_source_code)
