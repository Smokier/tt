from django.db import models


class FloatFieldConfig(models.Model):
    min_value = models.FloatField(null=True)
    max_value = models.FloatField(null=True)
    max_digits = models.IntegerField(null=True)
    decimal_places = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'FloatFieldConfig'
        verbose_name = 'Float Field Config'
        verbose_name_plural = 'Float Field Configs'
