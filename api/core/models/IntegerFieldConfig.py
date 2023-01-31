from django.db import models


class IntegerFieldConfig(models.Model):
    min_value = models.IntegerField(null=True)
    max_value = models.IntegerField(null=True)
    only_positive = models.BooleanField(default=False)
    big_integer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'IntegerFieldConfig'
        verbose_name = 'Integer Field Config'
        verbose_name_plural = 'Integer Field Configs'
