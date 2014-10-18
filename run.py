#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from zabiniec import config
from zabiniec.app import create_app
from zabiniec.utils import app_runner


parser = argparse.ArgumentParser(description="Uruchamia aplikacje")
parser.add_argument("--prod", help="włączenie trybu produkcyjnego")


def main():
    args = parser.parse_args()
    if args.prod:
        conf = config.ProductionConfig()
    else:
        conf = config.DevelopConfig()
    app = create_app(conf)
    app_runner(app, args.prod)


if __name__ == '__main__':
    main()
