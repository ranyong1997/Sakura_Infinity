# -*- coding: utf-8 -*-


from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers import OperateTypeSerializer
from element.models import OperateType


class OperateTypeViewSet(viewsets.ModelViewSet):
    """
    定位类型接口
    """
    permission_classes = (IsAuthenticated,)
    queryset = OperateType.objects.all()
    serializer_class = OperateTypeSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    #  ## 选择过滤
    filter_fields = ('id', 'operate_type')
