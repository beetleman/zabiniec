# -*- coding: utf-8 -*-
from inspect import getsource, getfile
from flask import session

from .utils import PROJECT_ROOT, porn

# Context Processors to takie cosie co są uruchamiane zaraz przed powstaniem
# kodu HTML który zostanie wysłany do przeglądarki
# kliknij przycis `PORN` a zobaczyrz ze `get_source_code` zawsze jet
# wykonywane ostatnie.


@porn
def get_source_code():
    """Funcja dodanie możliwość dostania się do wyuzdanych kodów w
    template dodaje do nich zmienna `source_code` jednocześnie
    kasuje zawartość `porn` w sesji aby powtorek nie było
    """
    porn = session.get('porn', [])
    session['porn'] = []
    return {'source_code': porn}


def register_context_processors(app):
    # rejestruje ten contekst procesor
    app.context_processor(get_source_code)
