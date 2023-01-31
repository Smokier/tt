from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import timedelta

from knox import crypto

sha = 'hashlib.sha512'

User = get_user_model()

class VerificationTokenManager(models.Manager):
    def create(
        self,
        user,
        expiry=timedelta(hours=24),
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


class AbstractVerificationToken(models.Model):

    objects = VerificationTokenManager()

    digest = models.CharField(
        max_length=128, primary_key=True)
    token_key = models.CharField(
        max_length=25,
        db_index=True
    )
    user = models.ForeignKey(User, null=False, blank=False,
                             related_name='verification_token_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s : %s' % (self.digest, self.user)


class VerificationToken(AbstractVerificationToken):
    pass
