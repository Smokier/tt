"""
URL mappings for the user API.
"""
from django.urls import path
from knox import views as knox_views
from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('auth/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logoutall/', views.LogoutAllView.as_view(), name='logoutall'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='resetpassword'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
