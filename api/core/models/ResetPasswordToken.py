from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import timedelta
from .AbstractToken import AbstractToken
from knox import crypto

sha = 'hashlib.sha512'

User = get_user_model()


class ResetPasswordTokenManager(models.Manager):
    def create(
        self,
        user,
        expiry= timedelta(hours=24),
        prefix=''
    ):
        token = prefix + crypto.create_token_string()
        digest = crypto.hash_token(token)
        if expiry is not None:
            expiry = timezone.now() + expiry
        instance = super(ResetPasswordTokenManager, self).create(
            token_key=token[:15], digest=digest,
            user=user, expiry=expiry)
        return instance, token


class ResetPasswordToken(AbstractToken):
    objects = ResetPasswordTokenManager()

    class Meta:
        db_table = 'ResetPasswordToken'
        verbose_name = 'Reset Password Token'
        verbose_name_plural = 'Reset Password Tokens'

    def __str__(self):
        return '%s : %s' % (self.digest, self.user)