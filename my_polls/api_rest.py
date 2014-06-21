#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from sandman import app

APP_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(APP_PATH, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + DB_PATH

from sandman.model import activate

activate(browser=False)

app.run()
