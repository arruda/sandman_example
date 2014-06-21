#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from sandman import app

APP_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(APP_PATH, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + DB_PATH


from sandman.model import register, activate, Model


class Poll(Model):
    __tablename__ = 'poll_poll'


class Vote(Model):
    __tablename__ = 'poll_vote'


class Item(Model):
    __tablename__ = 'poll_item'


class User(Model):
    __tablename__ = 'auth_user'

# # register can be called with an iterable or a single class
register((Poll, Vote, Item, User))

activate(browser=False)

app.run()
