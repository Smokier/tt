"""
Views for the user API.
"""
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from rest_framework.serializers import DateTimeField
from rest_framework import (
    generics,
    permissions,
    status,
    response
)


from knox.settings import knox_settings
from knox.auth import TokenAuthentication
from knox.views import (
    LoginView as KnoxLoginView,
    LogoutView as KnoxLogoutView,
    LogoutAllView as KnoxLogoutAllView
)

from drf_spectacular.utils import extend_schema

from core.schemes import KnoxTokenScheme
from core.models import (
    ResetPasswordToken,
    VerificationToken,
)
from user.serializers import (
    UserSerializer,
    UserMinimalSerializer,
    UserLoginSerializer,
    ResetPasswordSerializer,
)

from core.tasks import send_reset_password_email

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    # TODO add email verification
    # TODO add permissions
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserMinimalSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class LoginView(KnoxLoginView):
    """Authenticate a user and return a token."""
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def get_user_serializer_class(self):
        return UserMinimalSerializer

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return super(LoginView, self).post(request, format=None)


@extend_schema(request=None, responses=None)
class LogoutView(KnoxLogoutView):
    """Logout a user."""
    pass


@extend_schema(request=None, responses=None)
class LogoutAllView(KnoxLogoutAllView):
    """Logout user from all devices."""
    pass


class ResetPasswordView(generics.GenericAPIView):
    """Reset password for a user."""
    permission_classes = (permissions.AllowAny,)
    serializer_class = ResetPasswordSerializer

    def get_context(self):
        return {'request': self.request, 'format': self.format_kwarg, 'view': self}

    def get_token_limit_per_user(self):
        return knox_settings.TOKEN_LIMIT_PER_USER

    def get_expiry_datetime_format(self):
        return knox_settings.EXPIRY_DATETIME_FORMAT

    def format_expiry_datetime(self, expiry):
        datetime_format = self.get_expiry_datetime_format()
        return DateTimeField(format=datetime_format).to_representation(expiry)

    def create_token(self, user):
        instance, token = ResetPasswordToken.objects.create(
            user=user,
        )

        return instance, token

    def post(self, request, format=None):
        email = request.data.get('email')
        if email is None:
            return response.Response({'email': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)

        User = get_user_model()

        try:
            user = User.objects.get(email=email)

            if not user.is_active or not user.is_verified:
                raise ObjectDoesNotExist

            instance, token = self.create_token(user)

            if instance and token:
                send_reset_password_email.delay(instance.user.name, instance.user.last_name, instance.user.email, token)


            data = {'msg': 'Password reset email sent.',}
            return response.Response(data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return response.Response({'email': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)


