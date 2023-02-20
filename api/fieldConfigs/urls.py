from rest_framework import routers
from fieldConfigs import views
from django.urls import path, include

app_name = 'fieldConfigs'

router = routers.SimpleRouter()

router.register('date', views.DateFieldConfigViewSet)
router.register('float', views.FloatFieldConfigViewSet)
router.register('integer', views.IntegerFieldConfigViewSet)
router.register('char', views.CharFieldConfigViewSet)
router.register('foreign-key', views.ForeignKeyFieldConfigViewSet)
router.register('file', views.FileFieldConfigViewSet)
router.register('file/content-type', views.ContentTypeViewSet)
router.register('file/upload-size', views.UploadSizeViewSet)


urlpatterns = [
    path('', include(router.urls))
]
