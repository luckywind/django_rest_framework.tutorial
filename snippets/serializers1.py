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
'''
class SnippetSerializer(serializers.Serializer):
    '''
    定义序列化/反序列化的字段
    '''
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    '''
    create 和 update方法定义了在调用serializer.save()方法时，如何创建实例
    '''
    def create(self, validated_data):
        '''
        数据反序列化为实例 并返回
        :param validated_data:
        :return:
        '''
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''
        更新实例并返回
        :param instance:
        :param validated_data:
        :return:
        '''
        instance.title = validated_data.get('title', instance.title)
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

