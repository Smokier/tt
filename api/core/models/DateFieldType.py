from django.db import models

class DateFieldType(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'DateFieldType'
        verbose_name = 'Date Field Type'
        verbose_name_plural = 'Date Field Types'
