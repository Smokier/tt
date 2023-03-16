from django.db import models

class FileFieldConfig(models.Model):
    upload_to = models.CharField(max_length=255, null=False)
    max_length = models.IntegerField(null=False)
    max_bytes_upload_size = models.IntegerField(null=False, default=10)
    content_types = models.ForeignKey('ContentTypes', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'FileFieldConfig'
        verbose_name = 'File Field Config'
        verbose_name_plural = 'File Field Configs'
