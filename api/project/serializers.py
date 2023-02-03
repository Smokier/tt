from user.serializers import UserMinimalSerializer
from core.models import (
    Project,
    UserModel,
    Maintenance,
)

from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'customer')


class MaintenanceDataSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    user = UserMinimalSerializer()

    class Meta:
        model = Maintenance
        fields = ('id', 'project', 'user')
        depth = 1


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ('id', 'project', 'user')
