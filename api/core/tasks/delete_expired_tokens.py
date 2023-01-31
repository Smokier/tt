from celery import shared_task
from django.utils import timezone


from core.models import (
    ResetPasswordToken,
    VerificationToken,
)

@shared_task
def delete_expired_tokens():
    try:
        ResetPasswordToken.objects.filter(expires__lt=timezone.now()).delete()
    except Exception as e:
        return {'message': f'Error deleting expired reset password tokens'}
    try:
        VerificationToken.objects.filter(expires__lt=timezone.now()).delete()
    except Exception as e:
        return {'message': f'Error deleting expired verification tokens'}

    return {'message': 'Expired tokens deleted successfully.'}
