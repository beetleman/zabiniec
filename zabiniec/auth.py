# -*- coding: utf-8 -*-
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
