from django.db import models

class FileFieldConfig(models.Model):
    upload_to = models.CharField(max_length=255, null=False)
    max_length = models.IntegerField(null=False)
    content_types = models.ManyToManyField('ContentTypes', related_name='file_field_content_type_config')
    max_upload_size = models.ForeignKey('UploadSize', on_delete=models.CASCADE, null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'FileFieldConfig'
        verbose_name = 'File Field Config'
        verbose_name_plural = 'File Field Configs'
