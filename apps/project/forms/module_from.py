# -*- coding: utf-8 -*-

from django import forms
from ..models import Module


class ModuleCreateForm(forms.ModelForm):
    """
    新增环境表单
    """

    class Meta:
        model = Module
        exclude = ['maintainer']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ModuleCreateForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(ModuleCreateForm, self).save(commit=False)
        if self.request:
            obj.maintainer = self.request.user.username
        obj.save()
        return obj


class ModuleUpdateForm(ModuleCreateForm):
    """
    更新环境表单
    """

    def save(self, *args, **kwargs):
        obj = super(ModuleCreateForm, self).save(commit=False)  # 重写父类方法
        if self.request:
            obj.maintainer = self.request.user.username
        obj.save()
        return obj
