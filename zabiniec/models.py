# -*- coding: utf-8 -*-
from peewee import Model, CharField
from .database import get_db


class BaseModel(Model):
    class Meta:
        database = get_db()


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()

    class Meta:
        order_by = ('username',)
