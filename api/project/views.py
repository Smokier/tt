from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from project.serializers import (
    ProjectSerializer,
    ProjectDataSerializer,
    MaintenanceSerializer,
    MaintenanceDataSerializer,
    ProjectModelSerializer,
    ProjectModelDataSerializer,
    ProjectModelDataSerializer,
    ModelFieldSerializer,
)

from core.models import (
    Project,
    Maintenance,
    ProjectModel,
    ModelField,
)

from core.permissions import (
    isActiveUser,
    isMaintainer,
)

from rest_framework import permissions
from knox.auth import TokenAuthentication
from rest_framework import (
    viewsets,
    mixins,
    response,
    status,
    generics,
)


class ActiveProjectViewSet(viewsets.ModelViewSet):
    """Viewset for active projects"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, isActiveUser)
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        """List the all the active projects"""
        try:
            serializer = ProjectDataSerializer(self.queryset, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve an active project"""
        try:
            instance = self.get_object()
            serializer = ProjectDataSerializer(instance)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

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
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, isActiveUser)
    queryset = Project.objects.filter(is_active=False)
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        """List the all the active projects"""
        try:
            serializer = ProjectDataSerializer(self.queryset, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve an active project"""
        try:
            instance = self.get_object()
            serializer = ProjectDataSerializer(instance)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

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


class MaintenanceViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    #TODO Create the group for maintenance permissions
    """Viewset for maintenance"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, isActiveUser)
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

    def list(self, request, *args, **kwargs):
        """List the projects that the user is a maintainer"""
        try:
            serializer = MaintenanceDataSerializer(self.queryset, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class UserMaintenanceListView(generics.ListAPIView):
    """List the projects that the user is a maintainer"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, isActiveUser)
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    look_up_field = 'user'
    lookup_url_kwarg = 'id'


class ActiveProjectModelViewSet(viewsets.ModelViewSet):
    """Viewset for active project models"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, isActiveUser)
    queryset = ProjectModel.objects.filter(is_active=True)
    serializer_class = ProjectModelSerializer

    def list(self, request, *args, **kwargs):
        """List the all the active project models"""
        try:
            serializer = ProjectModelDataSerializer(self.queryset, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve an active project model"""
        try:
            instance = self.get_object()
            serializer = ProjectModelDataSerializer(instance)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Set the project model as inactive"""
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except (ObjectDoesNotExist, Http404):
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class InactiveProjectModelViewSet(mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
        """Viewset for inactive project models"""
        authentication_classes = (TokenAuthentication,)
        permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, isActiveUser)
        queryset = ProjectModel.objects.filter(is_active=False)
        serializer_class = ProjectModelSerializer

        def list(self, request, *args, **kwargs):
            """List the all the inactive project models"""
            try:
                serializer = ProjectModelDataSerializer(self.queryset, many=True)
                return response.Response(serializer.data, status=status.HTTP_200_OK)
            except (ObjectDoesNotExist, Http404):
                return response.Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return response.Response(status=status.HTTP_400_BAD_REQUEST)

        def retrieve(self, request, *args, **kwargs):
            """Retrieve a project model"""
            try:
                instance = self.get_object()
                serializer = ProjectModelDataSerializer(instance)
                return response.Response(serializer.data, status=status.HTTP_200_OK)
            except (ObjectDoesNotExist, Http404):
                return response.Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return response.Response(status=status.HTTP_400_BAD_REQUEST)

        def destroy(self, request, *args, **kwargs):
            """Set the project model as active"""
            try:
                instance = self.get_object()
                instance.is_active = True
                instance.save()
                return response.Response(status=status.HTTP_204_NO_CONTENT)
            except (ObjectDoesNotExist, Http404):
                return response.Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return response.Response(status=status.HTTP_400_BAD_REQUEST)


class ModelFieldViewSet(viewsets.ModelViewSet):
    """Viewset for model fields"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, isActiveUser)
    queryset = ModelField.objects.all()
    serializer_class = ModelFieldSerializer
