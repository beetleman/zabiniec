# -*- coding: utf-8 -*-
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from jinja2 import Markup

def pornomaker_filter(source):
    p = highlight(source, PythonLexer(), HtmlFormatter())
    return Markup(p)


def register_templatetags(app):
    app.jinja_env.filters['pornmaker'] = pornomaker_filter
