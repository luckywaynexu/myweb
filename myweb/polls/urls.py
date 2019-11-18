#  !/usr/bin/env  python
#  -*- coding:utf-8 -*-
# @Time   :  2019/10/21
# @Author :  xuwei
# @Email  :  mrwaynexue@126.com
# @Note   :
from django.urls import path
from . import views
urlpatterns = [
    path('', views.pollsapp),
    path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/vote', views.vote, name='vote'),
]