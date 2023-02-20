from django.urls import path, include
from project import views
from rest_framework import routers

app_name = 'project'

router = routers.SimpleRouter()

router.register('inactive', views.InactiveProjectViewSet, basename='inactive-project')
router.register('active', views.ActiveProjectViewSet, basename='active-project')
router.register('maintenance', views.MaintenanceViewSet, basename='maintenance')
router.register('models/', views.ActiveProjectModelViewSet, basename='active-project-model')
router.register('models/inactive', views.InactiveProjectModelViewSet, basename='inactive-project-model')
router.register('models/fields', views.ModelFieldViewSet, basename='model-field')
router.register('', views.ActiveProjectViewSet, basename='active-project')



urlpatterns = [
    path('maintenance/user/<int:id>/', views.UserMaintenanceListView.as_view(), name='maintenance-user'),
    path('', include(router.urls)),
]
