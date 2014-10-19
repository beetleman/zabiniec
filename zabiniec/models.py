# -*- coding: utf-8 -*-
from peewee import Model, CharField
from flask.ext.login import UserMixin

from .database import get_db


class BaseModel(Model):
    class Meta:
        database = get_db()


class User(BaseModel, UserMixin):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)

    class Meta:
        order_by = ('username',)
