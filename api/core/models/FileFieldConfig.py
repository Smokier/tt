from django.db import models

class FileFieldConfig(models.Model):
    upload_to = models.CharField(max_length=255, null=False)
    max_length = models.IntegerField(null=False)
    upload_size = models.ManyToManyField('UploadSize', related_name='file_field_config')
    created_at = models.DateTimeField(auto_now_add=True)
    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'FileFieldConfig'
        verbose_name = 'File Field Config'
        verbose_name_plural = 'File Field Configs'
