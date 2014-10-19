# -*- coding: utf-8 -*-
from flask.ext.login import LoginManager


def setup_auth(app):
    from .models import User
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(userid):
        return User.get(User.get(User.id == userid))
