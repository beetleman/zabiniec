# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

from flask import Flask


def create_app(config):
    """Funkcja tworząca aplikacje i konfigurująca ją.

    :param config: Objekt z konfiguracja aplikacji
    :returns: aplikacje flask
    :rtype: flask.Flask

    """
    # tworze objekt flask
    app = Flask(__name__)
    # karze mu wczytać konfugyracje
    app.config.from_object(config)
    # wszystko co związane z aplikacja musi być uruchomione w jej kontekście,
    # poproś Trolla Marnego o wytłumaczenie co to znaczy:D
    # dzięki temu możemy używać zmiennej globalnej Flask.g
    with app.app_context():
        # tworzenie bazydanych
        from .database import create_db
        create_db(app)
        # przygotowuje obsługę sesji, nie musisz znać jej implementacji.
        from flask_kvsession import KVSessionExtension
        KVSessionExtension(app.config['SESSION_STORE_CREATOR'](), app)
        # przygotowuje takie cosie co dodaja różne rzeczy dla template
        # sprawdź plik context_processors.py dla większej ilości informacji
        from .context_processors import register_context_processors
        register_context_processors(app)
        # to też sprawy związane z template, Troll musi Lady Nadzianej
        # wytłumaczyć ich ideę to Żabka zrozumii:*
        from .templatetags import register_templatetags
        register_templatetags(app)
        # tworzenie takiego czegoś co odpowiada za to ze w odpowiedzi na dany
        # adrest aplikacja wykona odpowiednia funkccje, ja Zaba zobaczy
        # plik to załapie:*
        from .routes import create_routes
        create_routes(app)
        # Rzeczy związane z logowaniem, to zostaw Kochanie na poźniej:*
        from .auth import setup_auth
        setup_auth(app)
    return app
