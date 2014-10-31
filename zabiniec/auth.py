# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

from flask.ext.login import LoginManager

from .utils import porn


def setup_auth(app):
    """Konfiguracja autoryzacji dla aplikacji

    :param app: Aklickaja flask
    """

    # importuje model który ustawie jako model użytkowników
    # więcej na: https://flask-login.readthedocs.org/en/latest/
    from .models import User
    login_manager = LoginManager()
    login_manager.init_app(app)

    # ustawiam na jaki adres maja byś przerzucane wywołania
    # adresów na strony na ktore nie ma sie uprawnień
    login_manager.login_view = "index"

    @login_manager.user_loader
    @porn
    def load_user(userid):
        return User.get(User.id == userid)
