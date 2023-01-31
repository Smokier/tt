from django.db import models


class UploadSize(models.Model):
    UPLOAD_SIZE_CHOICES = (
        ('2MB', 2621440),
        ('5MB', 5242880),
        ('10MB', 10485760),
    )

    name = models.CharField(max_length=255, null=False)
    size = models.IntegerField(choices=UPLOAD_SIZE_CHOICES, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'UploadSize'
        verbose_name = 'Upload Size'
        verbose_name_plural = 'Upload Sizes'

    def __str__(self):
        return self.name
