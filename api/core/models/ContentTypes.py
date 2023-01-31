from django.db import models


class ContentTypes(models.Model):
    name = models.CharField(max_length=255, null=False)
    content_types = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ContentTypes'
        verbose_name = 'Content Type'
        verbose_name_plural = 'Content Types'

    def __str__(self):
        return self.name
