#!/usr/bin/env python
# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

from zabiniec import config
from zabiniec.app import create_app


def main():
    """Główna funkcja programu, to ona startuje wszystko. Uruchamia w trybie do żabawy,
    to znaczy ze tym plikiem nie powinno sie uruchamiać aplikacji na hostingu.
    """
    app = create_app(config.DevelopConfig())
    app.run()


if __name__ == '__main__':
    # Funkcja main jest wykonywana tylko wtedy gdy plik run.py
    # jest uruchomiony jako program
    main()
