# -*- coding: utf-8 -*-
from flask.ext.login import LoginManager

from .utils import porn


def setup_auth(app):
    from .models import User
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "index"

    @login_manager.user_loader
    @porn
    def load_user(userid):
        return User.get(User.id == userid)
