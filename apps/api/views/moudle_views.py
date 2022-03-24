# -*- coding: utf-8 -*-


from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers import ModuleSerializer
from project.models import Module


class ModuleViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    项目信息接口
    """
    permission_classes = (IsAuthenticated,)
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ## 选择过滤
    filter_fields = ("id", "projcet", "module_name", "module_alias", "isenabled", "updatetime", "maintainer",)
