# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       chengxingfu
   date：          2019/4/28
-------------------------------------------------
   Change Activity:
                   2019/4/28:
-------------------------------------------------
"""
from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet

__author__ = 'chengxingfu'
'''
实例序列化为json的和反序列化的一种方式，声明一个serializers，  它非常类似django的Form类
SnippetSerializer 类重复了snippet模型的信息，使用ModelSerializer可以简化：
1、自动决定字段集
2、默认create()和update()实现
'''
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

