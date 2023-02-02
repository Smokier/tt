from django.urls import path, include
from project import views
from rest_framework import routers

app_name = 'project'

router = routers.SimpleRouter()

router.register('inactive', views.InactiveProjectViewSet, basename='inactive-prkject')
router.register('', views.ActiveProjectViewSet, basename='active-project')


urlpatterns = [
    path('', include(router.urls))
]
