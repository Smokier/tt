from rest_framework import permissions
from core.models import (
    ProjectModel,
    Maintenance,
    ModelField,
    FileFieldConfig,
    IntegerFieldConfig,
    CharFieldConfig,
    ForeignKeyFieldConfig,
    FloatFieldConfig,
    DateFieldConfig,
)


class isMaintainer(permissions.BasePermission):
    def has_permission(self, request, view):

        pass

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        if isinstance(obj, ProjectModel):
            return Maintenance.objects.filter(project=obj.project, user=request.user).exists()
        
        if isinstance(obj, ModelField):
            return Maintenance.objects.filter(project=obj.project_model.project, user=request.user).exists()
        
        if isinstance(obj, FileFieldConfig):
            return Maintenance.objects.filter(project=obj.model_field.project_model.project, user=request.user).exists()
        
        if isinstance(obj, IntegerFieldConfig):
            return Maintenance.objects.filter(project=obj.model_field.project_model.project, user=request.user).exists()
        

        return False
