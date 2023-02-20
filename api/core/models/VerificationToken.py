from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import timedelta
from .AbstractToken import AbstractToken
from knox import crypto

sha = 'hashlib.sha512'

User = get_user_model()

class VerificationTokenManager(models.Manager):
    def create(
        self,
        user,
        expiry=timedelta(hours=48),
        prefix=''
    ):
        token = prefix + crypto.create_token_string()
        digest = crypto.hash_token(token)
        if expiry is not None:
            expiry = timezone.now() + expiry
        instance = super(VerificationTokenManager, self).create(
            token_key=token[:15], digest=digest,
            user=user, expiry=expiry)
        return instance, token


class VerificationToken(AbstractToken):
    objects = VerificationTokenManager()

    class Meta:
        db_table = 'VerificationToken'
        verbose_name = 'Verification Token'
        verbose_name_plural = 'Verification Tokens'

    def __str__(self):
        return '%s : %s' % (self.digest, self.user)
