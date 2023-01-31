from django.db import models


class DateFieldConfig(models.Model):
    DATE_FIELD_TYPE = (
        ('date', 'Date'),
        ('datetime', 'Date Time'),
        ('time', 'Time'),
    )
    type = models.CharField(max_length=255, null=False, choices=DATE_FIELD_TYPE)
    auto_now = models.BooleanField(default=False)
    auto_now_add = models.BooleanField(default=False)
    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'DateFieldConfig'
        verbose_name = 'Date Field Config'
        verbose_name_plural = 'Date Field Configs'

    def __str__(self):
        return self.name
