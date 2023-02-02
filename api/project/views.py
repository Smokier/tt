from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from project.serializers import (
    ProjectSerializer,
)

from core.models import (
    Project,
)

from rest_framework import permissions
from knox.auth import TokenAuthentication
from rest_framework import (
    viewsets,
    mixins,
    response,
    status
)

class ActiveProjectViewSet(viewsets.ModelViewSet):
    """Viewset for active projects"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer

    def destroy(self, request, *args, **kwargs):
        """Set the project as inactive"""
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class InactiveProjectViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    """Viewset for inactive projects"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = Project.objects.filter(is_active=False)
    serializer_class = ProjectSerializer

    def destroy(self, request, *args, **kwargs):
        """Set the project as active"""
        try:
            instance = self.get_object()
            instance.is_active = True
            instance.save()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


