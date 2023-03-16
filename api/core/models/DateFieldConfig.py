from django.db import models


class DateFieldConfig(models.Model):
    auto_now = models.BooleanField(default=False)
    auto_now_add = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date_field_type = models.ForeignKey('DateFieldType', on_delete=models.CASCADE, null=False, default=1)
    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'DateFieldConfig'
        verbose_name = 'Date Field Config'
        verbose_name_plural = 'Date Field Configs'

    def __str__(self):
        return self.name
