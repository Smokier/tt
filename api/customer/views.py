from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from core.models import Customer
from customer.serializers import CustomerSerializer
from knox.auth import TokenAuthentication
from rest_framework import (
    viewsets,
    permissions,
    status,
    response,
    mixins
)


class ActiveCustomerViewSet(viewsets.ModelViewSet):
    """Viewset for active customers"""
    serializer_class = CustomerSerializer
    queryset = Customer.objects.filter(is_active=True)
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        """Set the customer as inactive"""
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            return response.Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class InactiveCustomerViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
#class InactiveCustomerViewSet(viewsets.ModelViewSet):
    """Viewset for inactive customers"""
    serializer_class = CustomerSerializer
    queryset = Customer.objects.filter(is_active=False)
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        return Customer.objects.filter(is_active=False)

    def destroy(self, request, *args, **kwargs):
        """Set the customer as active"""
        try:
            instance = self.get_object()
            instance.is_active = True
            instance.save()
            return response.Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


