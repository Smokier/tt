from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from core.models import DataType
from dataType.serializers import DataTypeSerializer

from knox.auth import TokenAuthentication
from rest_framework import (
    viewsets,
    mixins,
    response,
    status,
    permissions,
)


class ActiveDataTypeViewSet(viewsets.ModelViewSet):
    """Viewset for active data types"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = DataType.objects.filter(is_active=True)
    serializer_class = DataTypeSerializer

    def destroy(self, request, *args, **kwargs):
        """Set the data type as inactive"""
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class InactiveDataTypeViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
        """Viewset for inactive data types"""
        authentication_classes = (TokenAuthentication,)
        permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
        queryset = DataType.objects.filter(is_active=False)
        serializer_class = DataTypeSerializer

        def destroy(self, request, *args, **kwargs):
            """Set the data type as active"""
            try:
                instance = self.get_object()
                instance.is_active = True
                instance.save()
                return response.Response(status=status.HTTP_204_NO_CONTENT)
            except (ObjectDoesNotExist, Http404):
                return response.Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return response.Response(status=status.HTTP_400_BAD_REQUEST)
