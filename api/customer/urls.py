from django.urls import path, include
from customer import views
from rest_framework import routers

app_name = 'customer'

router = routers.SimpleRouter()

router.register(r'inactive', views.InactiveCustomerViewSet, basename='inactive-customer')
router.register(r'', views.ActiveCustomerViewSet, basename='active-customer')


urlpatterns = [
    path('', include(router.urls)),
]
