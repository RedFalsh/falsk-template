#!/usr/bin/env python
# encoding: utf-8

from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app.model import db, Template

admin = Admin(name='后台管理', template_mode = 'bootstrap3')

class TemplateModelAdmin(ModelView):
    can_create = True # disable model create
    can_edit = True # disable model edit
    can_delete = True # disable model delete
    can_view_details = False  # 显示细节

    # 可姓名、电话进行搜索
    # column_searchable_list = ['name']
    # 按名字过滤
    # column_filters = ['name']

    column_labels = {
        'name':'姓名'
    }

admin.add_view(TemplateModelAdmin(Template, db.session, category='模板'))


