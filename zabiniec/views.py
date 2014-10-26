# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from flask.ext.login import login_user, login_required, logout_user, current_user

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


@login_required
@porn
def change_passwd():
    is_failed = False
    complementary_user = current_user.get_complementary()
    if request.method == 'POST':
        answer = request.form.get('answer', None)
        question = request.form.get('question', None)
        if len(question) < 10 and len(answer) < 5:
            is_failed = True
        else:
            complementary_user.answer = answer
            complementary_user.question = question
            complementary_user.save()

    return render_template(
        'change_passwd.html',
        title='Hasła zmienianie, śąwiata zaskakiwanie',
        is_failed=is_failed,
        answer=complementary_user.answer,
        question=complementary_user.question
    )
