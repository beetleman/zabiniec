# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from jinja2 import Markup

# plik z temlate tagami czy z nowymi słowami kluczowymi które
# można urywać w templte ja potrzebowałem czegoś co
# pokoloruje mi kod z pornolami:D


def pornomaker_filter(source):
    """funkcja która koloruje pornole

    :param source: plik źródłowy Python do pokolorowania
    :returns: HTML z pokolorowanym kodem
    :rtype: jinja2.Markup

    """
    p = highlight(source, PythonLexer(), HtmlFormatter())
    return Markup(p)


def register_templatetags(app):
    app.jinja_env.filters['pornmaker'] = pornomaker_filter
