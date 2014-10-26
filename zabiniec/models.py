# -*- coding: utf-8 -*-
import datetime
from peewee import (
    Model, CharField, TextField, ForeignKeyField,
    BooleanField, DateTimeField
)
from flask.ext.login import UserMixin

from .database import get_db


class BaseModel(Model):
    created = DateTimeField(default=datetime.datetime.now)
    modified = DateTimeField()

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = get_db()


class App(BaseModel):
    initialized = BooleanField(default=False)


class User(BaseModel, UserMixin):
    TROLL = 'troll'
    ZABKA = 'zabka'
    username = CharField(unique=True, max_length=20)
    question = CharField(max_length=100)
    answer = CharField(max_length=100)
    email = CharField(unique=True, max_length=100, null=True)

    def is_zabka(self):
        return self.username == self.ZABKA

    def is_troll(self):
        return self.username == self.TROLL

    def get_complementary(self):
        if self.username == self.ZABKA:
            username = self.TROLL
        elif self.username == self.TROLL:
            username = self.ZABKA
        else:
            usenname = None
        return User.get(username=username)

    class Meta:
        order_by = ('username',)


class List(BaseModel):
    title = CharField(max_length=100, default="")
    description = TextField(default="")
    author = ForeignKeyField(
        User,
        related_name='lists',
        on_delete='CASCADE',
    )

    def is_done(self):
        for field in self.fields:
            if not field.done:
                return False
        return True


class ListField(BaseModel):
    todo = CharField(max_length=200)
    done = BooleanField(default=False)
    done_by = ForeignKeyField(
        User,
        related_name='done',
        on_delete='CASCADE',
        null=True
    )
    list = ForeignKeyField(
        List,
        related_name='fields',
        on_delete='CASCADE',
    )

    def save(self, *args, **kwargs):
        self.list.save()
        return super(ListField, self).save(*args, **kwargs)
