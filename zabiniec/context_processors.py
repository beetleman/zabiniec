# -*- coding: utf-8 -*-
from inspect import getsource, getfile
from flask import g

from .utils import PROJECT_ROOT, porn


@porn
def get_source_code():
    source_code = []
    if hasattr(g, 'porn'):
        for obj in g.porn:
            title = getfile(obj).replace(PROJECT_ROOT, 'zabiniec')
            source_code.append({
                'title': title,
                'content': getsource(obj)
            })
        g.porn = []
    source_code.reverse()
    return {'source_code': source_code}


def register_context_processors(app):
    app.context_processor(get_source_code)
