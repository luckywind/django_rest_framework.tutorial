# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       chengxingfu
   date：          2019/4/28
-------------------------------------------------
   Change Activity:
                   2019/4/28:
-------------------------------------------------
"""
from rest_framework.routers import DefaultRouter

__author__ = 'chengxingfu'
from django.conf.urls import url, include
from snippets import views


'''
    NOTE:
    1 一旦匹配成功则不再继续
    2 若要从URL 中捕获一个值，只需要在它周围放置一对圆括号。
    3 不需要添加一个前导的反斜杠，因为每个URL 都有。例如，应该是^articles 而不是 ^/articles。
    4 每个正则表达式前面的'r' 是可选的但是建议加上。
    5 ()包起来的参数将传递给视图函数
'''
urlpatterns = [
    url('snippets$', views.snippet_list),  #注意url的正则写法，开头没有^ 和/
    # url('snippets/<int:pk>', views.snippet_detail), #django2.x的语法
    url('snippets/(?P<pk>\d+)',views.snippet_detail),  #django1.x捕获路径参数使用正则，有名分组，组语法是(?P<name>pattern)
    # url(r'^articles/([0-9]{4})/$', views.year_archive), # 无名分组，表示匹配4个0-9的任意数字

]