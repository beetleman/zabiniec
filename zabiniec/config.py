# -*- coding: utf-8 -*-
from peewee import SqliteDatabase, PostgresqlDatabase
from simplekv.fs import FilesystemStore

from .utils import get_abspath


class Conf:

    """Klasa przechowująca ogólny schemat konfiguracji.
    """

    # sekretny klucz używany do podpisywania ciasteczek
    # związanych z sesją
    SECRET_KEY = '_zw_fhfv#affd@2**k9*i-f*coh&gu@p@o(f=f-i6m8mr7#u!g'
    DB_CLASS = None
    DB_NAME = None
    DB_HOST = None
    DB_PASSWORD = None
    SESSION_STORE = None


class DevelopConfig(Conf):
    # w czasie rozwijania aplikacji używam sqlite
    DB_CLASS = SqliteDatabase
    # włączam flagę debug, co powoduje ze jak coś się zepsuje to
    # aplikacja mówi dokładnie gdzie, to jest funkcjonalność zapewniona przez
    # flask.
    DEBUG = True
    # lokalizacja pliku z bazą
    DB_NAME = get_abspath('dane.db')
    # ustawienie sesji na taka która jest przechowywana w katalogu
    # by Żabka mogla podejrzeć co się wyrabia:D
    SESSION_STORE = FilesystemStore(get_abspath('session'))


# wybacz kotek ale nie zdąrzył Marny Troll:(
class ProductionConfig(Conf):
    DB_CLASS = PostgresqlDatabase
    DEBUG = False
    # TODO: dopisać ustawianie dla pg
