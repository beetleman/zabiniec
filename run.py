#!/usr/bin/env python
# -*- coding: utf-8 -*-

# aby dziaałało tak samo na python 2 i 3, znaczy z 2.7 robię 3.x :D
from __future__ import (absolute_import, division, unicode_literals,
                        print_function, nested_scopes)

import argparse

from zabiniec import config
from zabiniec.app import create_app
from zabiniec.utils import app_runner


parser = argparse.ArgumentParser(description="Uruchamia aplikacje")
parser.add_argument(
    "-p",
    "--prod",
    help="włączenie trybu produkcyjnego",
    action='store_true'
)


def main():
    """Główna funkcja programu, to ona startuje wszystko.
    """
    # przygotowuje parser dla argumentów do programu run.py
    args = parser.parse_args()
    # w zależności od parametru --prod strona uruchamia
    # sie w trybybie produkcyjnym lub nie
    if args.prod:
        conf = config.ProductionConfig()
    else:
        conf = config.DevelopConfig()
    # uruchamiam aplikacje
    app = create_app(conf)
    app_runner(app, args.prod)


if __name__ == '__main__':
    # Funkcja main jest wykonywana tylko wtedy gdy plik run.py
    # jest uruchomiony jako program
    main()
