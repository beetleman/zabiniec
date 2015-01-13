#!/usr/bin/env python
# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

from zabiniec import config
from zabiniec.app import create_app

app = create_app(config.ProductionConfig())
