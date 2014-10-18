# -*- coding: utf-8 -*-
from flask import render_template

from .utils import porn


@porn
def index():
    return render_template('index.html', title='index')
