from django.db import models


class CharFieldConfig(models.Model):
    max_length = models.IntegerField(null=False)
    regex_pattern = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'CharFieldConfig'
        verbose_name = 'Char Field Config'
        verbose_name_plural = 'Char Field Configs'
