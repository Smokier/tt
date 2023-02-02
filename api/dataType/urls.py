from rest_framework import routers
from dataType import views
from django.urls import path, include

app_name = 'dataType'

router = routers.SimpleRouter()

router.register('inactive', views.InactiveDataTypeViewSet, basename='inactive-data-type')
router.register('', views.ActiveDataTypeViewSet, basename='active-data-type')


urlpatterns = [
    path('', include(router.urls))
]
