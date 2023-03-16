from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework import permissions
from knox.auth import TokenAuthentication
from rest_framework import (
    viewsets,
)


from core.models import (
    DateFieldConfig,
    FloatFieldConfig,
    IntegerFieldConfig,
    CharFieldConfig,
    ForeignKeyFieldConfig,
    FileFieldConfig,
)

from fieldConfigs.serializers import (
    DateFieldConfigSerializer,
    FloatFieldConfigSerializer,
    IntegerFieldConfigSerializer,
    CharFieldConfigSerializer,
    ForeignKeyFieldConfigSerializer,
    FileFieldConfigSerializer,
)

from core.permissions import (
    isActiveUser,
    isMaintainer,
)


class DateFieldConfigViewSet(viewsets.ModelViewSet):
    """Viewset for date field configurations"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, isActiveUser)
    queryset = DateFieldConfig.objects.all()
    serializer_class = DateFieldConfigSerializer


class IntegerFieldConfigViewSet(viewsets.ModelViewSet):
    """Viewset for integer field configurations"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, isActiveUser)
    queryset = IntegerFieldConfig.objects.all()
    serializer_class = IntegerFieldConfigSerializer


class FloatFieldConfigViewSet(viewsets.ModelViewSet):
    """Viewset for float field configurations"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, isActiveUser)
    queryset = FloatFieldConfig.objects.all()
    serializer_class = FloatFieldConfigSerializer


class CharFieldConfigViewSet(viewsets.ModelViewSet):
    """Viewset for char field configurations"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, isActiveUser)
    queryset = CharFieldConfig.objects.all()
    serializer_class = CharFieldConfigSerializer


class ForeignKeyFieldConfigViewSet(viewsets.ModelViewSet):
    """Viewset for foreign key field configurations"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, isActiveUser)
    queryset = ForeignKeyFieldConfig.objects.all()
    serializer_class = ForeignKeyFieldConfigSerializer


class FileFieldConfigViewSet(viewsets.ModelViewSet):
    """Viewset for file field configurations"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, isActiveUser)
    queryset = FileFieldConfig.objects.all()
    serializer_class = FileFieldConfigSerializer
