# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

from flask import render_template, request, redirect, url_for, abort
from flask.ext.login import login_user, login_required, logout_user, \
    current_user

from .utils import porn
from .models import User, List, ListField

# to coś z @ to dodanie dekoratora do danej funkcji,
# dekorator porn napisał Troll, a login_required
# jak nazwa wskazuje sprawdza czy jest się zalogowanym

# w tym dokumencie są tylko funkcje które zwracają albo
# przekierowanie lub coś co będzie htmlem


@porn
def index():
    """główna strona
    """
    if not current_user.is_anonymous() and current_user.is_authenticated():
        return redirect(url_for('lists'))
    return render_template('index.html', title='Ktoś?')


@porn
def login():
    """Strona logowania
    """
    # jeśli ktoś jest zalogowany to się go przerzuca
    # od razu do strony z listami
    if not current_user.is_anonymous() and current_user.is_authenticated():
        return redirect(url_for('lists'))

    # bierzemy parametr przekazany w adresie,
    # sprawdź co masz w pasku przeglądarki to sie domyślisz,
    # będzie coś w rodzaju `/login?kto=zabka`
    username = request.args.get('kto')
    is_failed = False
    try:
        user = User.get(User.username == username)
    except User.DoesNotExist:
        # jeśli nie ma użytkownika to znaczy ze ktoś cos kombinuje,
        # przekierować do strony w której może sobie kliknąć kim jest
        return redirect(url_for('index'))
    # jeśli dane są przekazywane postem to obsługa logowanie
    # jak nie to wy-renderowanie formularza z danymi do logowania
    if request.method == 'POST':
        answer = request.form.get('answer')
        # sprawdzam czy dobrze odpowiedziano na pytanie,
        # ignoruje wielkość znaków
        # (.lower() powoduje ze wszytko zmienione zostaje na małe literki)
        if answer.lower() == user.answer.lower():
            # jak dobrze dopowiedziane to przekierowuje na stronę z listami
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
    """wylogowywanie użytkownika obecnego w obecnej sesji
    """
    logout_user()
    return redirect(url_for('index'))


@login_required
@porn
def lists():
    """Popranie wszystkich list i przekazanie ich do template
    do wyświetlenia
    """
    return render_template(
        'lists.html',
        title='Planista-Żabista!',
        lists=List.select()
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


@porn
def _edit_list_helper(obj):
    description = request.form.get('description', '').strip()
    title = request.form.get('title', '').strip()
    if len(description) < 5 or len(title) < 5:
        return (obj, False)
    obj.description = description
    obj.title = title
    obj.author = current_user.id
    obj.save()

    for todo in request.form.getlist('todo'):
        # czyszcze z pustych wpisów
        if not todo.strip() and len(todo.strip()) < 5:
            continue
        ListField(todo=todo, list=obj.id).save()

    for key in request.form.keys():
        if 'todo_' in key:
            _, field_id = key.split('_')
            field = ListField.get(id=field_id, list=obj.id)
            field.todo = request.form.get(key)
            field.save()

    return (obj, True)


@login_required
@porn
def edit_list(list_id=None):
    try:
        list_obj = List.get(id=list_id)
    except List.DoesNotExist:
        abort(404)
    is_done = True
    if request.method == 'POST':
        list_obj, is_failed = _edit_list_helper(list_obj)
    return render_template(
        'edit_list.html',
        title='Tego kce!',
        is_failed=not is_done,
        list_obj=list_obj
    )


@login_required
@porn
def add_list():
    list_obj = List()
    is_done = True
    if request.method == 'POST':
        list_obj, is_done = _edit_list_helper(list_obj)
        if is_done:
            return redirect(url_for('edit_list', list_id=list_obj.id))
    return render_template(
        'edit_list.html',
        title='Tego kce!',
        is_failed=not is_done,
        list_obj=list_obj
    )


@login_required
@porn
def delete_list(list_id=None):
    try:
        list_obj = List.get(id=list_id)
    except List.DoesNotExist:
        abort(404)
    list_obj.delete_instance(recursive=True)
    return redirect(url_for('lists'))


@login_required
@porn
def delete_listfield(list_id=None, field_id=None):
    try:
        field_obj = ListField.get(id=field_id, list=list_id)
    except List.DoesNotExist:
        abort(404)
    field_obj.delete_instance()
    return redirect(url_for('edit_list', list_id=list_id))


@login_required
@porn
def view_list(list_id=None):
    try:
        list_obj = List.get(id=list_id)
    except List.DoesNotExist:
        abort(404)
    return render_template(
        'view_list.html',
        title='Co robimy?',
        list_obj=list_obj
    )


@login_required
@porn
def toggle_listfield(list_id=None, field_id=None):
    try:
        field_obj = ListField.get(id=field_id, list=list_id)
    except List.DoesNotExist:
        abort(404)
    if not field_obj.can_i(current_user):
        abort(401)
    field_obj.done = not field_obj.done
    if field_obj.done:
        field_obj.done_by = current_user.id
    field_obj.save()
    return redirect(url_for('view_list', list_id=list_id))
