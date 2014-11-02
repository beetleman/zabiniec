# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

from peewee import SqliteDatabase, PostgresqlDatabase
from simplekv.fs import FilesystemStore

from .peeweestore import PeeweeStore
from .database import get_db
from .utils import get_abspath


class Conf:

    """Klasa przechowująca ogólny schemat konfiguracji.
    """

    # sekretny klucz używany do podpisywania ciasteczek
    # związanych z sesją
    SECRET_KEY = '_zw_fhfv#affd@2**k9*i-f*coh&gu@p@o(f=f-i6m8mr7#u!g'
    # lokalizacja pliku z bazą
    DB_NAME = get_abspath('dane.db')
    DB_HOST = None
    DB_PASSWORD = None


class DevelopConfig(Conf):
    # w czasie rozwijania aplikacji używam sqlite
    # włączam flagę debug, co powoduje ze jak coś się zepsuje to
    # aplikacja mówi dokładnie gdzie, to jest funkcjonalność zapewniona przez
    # flask.
    DEBUG = True
    DB_CLASS = SqliteDatabase
    # ustawienie sesji na taka która jest przechowywana w katalogu
    # by Żabka mogla podejrzeć co się wyrabia:D
    SESSION_STORE_CREATOR = lambda self: FilesystemStore(
        get_abspath('session'))
    # lambda to jest takie coś do szybszego zapisywania funkcji
    # http://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie/Wyra%C5%BCenia_lambda


class ProductionConfig(Conf):
    DEBUG = False
    SESSION_STORE_CREATOR = lambda self: PeeweeStore(get_db())
    DB_CLASS = PostgresqlDatabase
    APP_HOST = '0.0.0.0'
    APP_PORT = '18001'
    APP_PID_FILE = get_abspath('pid')
