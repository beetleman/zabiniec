# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

import datetime
from peewee import (
    Model, CharField, TextField, ForeignKeyField,
    BooleanField, DateTimeField
)
from flask.ext.login import UserMixin

from .database import get_db
from .utils import porn


class BaseModel(Model):

    """klasa matka dla wszystkich klas modeli, ustawia dla nich pewne stałe
    elementy, np. bazę danych czy pola przechowujące kiedy coś zostało
    stworzone lub zmodyfikowane.
    """

    # automatycznie tworzone z aktualna data kiedy powstaje
    # nowy obiekt klasy dziedziczącej z BaseModel
    created = DateTimeField(default=datetime.datetime.now)
    modified = DateTimeField()

    def save(self, *args, **kwargs):
        # uaktualnia dane kiedy nastąpiła modyfikacja
        self.modified = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = get_db()


# to tylko po to by wiedzieć czy aplikacja się zainicjowała
class App(BaseModel):
    initialized = BooleanField(default=False)


class User(BaseModel, UserMixin):
    TROLL = 'troll'
    ZABKA = 'zabka'
    username = CharField(unique=True, max_length=20)
    question = CharField(max_length=100)
    answer = CharField(max_length=100)
    email = CharField(unique=True, max_length=100, null=True)

    @porn
    def is_zabka(self):
        """sprawdzamy czy użytkownik jest Żabą Naczelną

        :returns: rezultat testu
        :rtype: Bool

        """
        return self.username == self.ZABKA

    @porn
    def is_troll(self):
        """sprawdzamy czy użytkownik jest Marnym Trollem

        :returns: rezultat testu
        :rtype: Bool

        """
        return self.username == self.TROLL

    @porn
    def get_complementary(self):
        """Szukamy towarzystwa dla użytkownika

        :returns: komplementarny użytkownik
        :rtype: User

        """

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

    def complete_percent(self):
        """Sprawdza kompletność zadania

        :returns: Procent ukonczenia
        :rtype: Float

        """
        done = 0
        for field in self.fields:
            if field.done:
                done += 1
        return float(done) * 100 / self.fields.count()

    @porn
    def is_done(self):
        """Sprawdza czy lista ukończona

        :returns: wynik testu
        :rtype: Bool

        """
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

    def can_i(self, user):
        """Sprawdza czy dany użytkownik może coś zrobić
        z danym polem na liście, tylko urzytkownik który zaznaczył ze coś
        zrobił może to odznaczyć

        :param user: User
        :returns: wynik testu
        :rtype: Bool

        """
        if not self.done or (self.done and user.id == self.done_by.id):
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        # każda zmiana pola jest liczona jako zmiana listy wiec
        # wywodujemy metodę save listy aby zaktualizowała też swoją
        # datę

        self.list.save()
        # wywołujemy metodę save tej klasy, tą którą tutaj nadpisujemy.
        return super(ListField, self).save(*args, **kwargs)
