from rest_framework import permissions
from core.models import Maintenance


class isMaintainer(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        is_maintainer = Maintenance.objects.filter(
            user=request.user,
            project=obj
        ).exists()

        return is_maintainer
