#!/usr/bin/env python
# encoding: utf-8

from app import db

class Template(db.Model):
    __tablename__ = 'tmp'

    id          = db.Column(db.BigInteger, primary_key=True)
    name     = db.Column(db.String(100))
    updated_time = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<id {}>'.format(self.id)

