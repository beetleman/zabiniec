# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from flask.ext.login import login_user, login_required, logout_user

from .utils import porn
from .models import User


@porn
def index():
    return render_template('index.html', title='Ktoś?')


@porn
def login():
    username = request.args.get('kto')
    is_failed = False
    try:
        user = User.get(User.username == username)
    except User.DoesNotExist:
        return redirect(url_for('index'))
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer.lower() == user.answer.lower():
            login_user(user)
            return redirect(url_for('lists'))
        else:
            is_failed = True
    return render_template(
        'login.html',
        title='Że jak?',
        question=user.question,
        username=username,
        is_failed=is_failed
    )


@login_required
@porn
def logout():
    logout_user()
    return redirect(url_for('index'))


@login_required
@porn
def lists():
    return render_template(
        'lists.html',
        title='Planista-Żabista!',
    )
