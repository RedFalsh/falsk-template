#!/usr/bin/env python
# encoding: utf-8



from flask import Blueprint, render_template
from app import db

index = Blueprint('index', __name__,
                 template_folder='templates',
                 static_folder='static')

@index.route('/')
def home():
    return 'Whelecome My Flask Example'

