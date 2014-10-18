# -*- coding: utf-8 -*-
import os
from peewee import SqliteDatabase, PostgresqlDatabase

from .utils import get_abspath


class Conf:
    SECRET_KEY = '_zw_fhfv#affd@2**k9*i-f*coh&gu@p@o(f=f-i6m8mr7#u!g'
    DB_CLASS = None
    DB_NAME = None
    DB_HOST = None
    DB_PASSWORD = None


class DevelopConfig(Conf):
    DB_CLASS = SqliteDatabase
    DEBUG = True
    DB_NAME = get_abspath('dane.db')


class ProductionConfig(Conf):
    DB_CLASS = PostgresqlDatabase
    DEBUG = False
    # TODO: dopisać ustawianie dla pg
