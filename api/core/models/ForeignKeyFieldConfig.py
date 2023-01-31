from django.db import models


class ForeignKeyFieldConfig(models.Model):
    RELATION_TYPES = (
        ('1', 'One to One'),
        ('2', 'One to Many'),
        ('3', 'Many to Many'),
    )

    relation_type = models.CharField(max_length=1, choices=RELATION_TYPES, null=False)
    on_delete = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'ForeignKeyFieldConfig'
        verbose_name = 'Foreign Key Field Config'
        verbose_name_plural = 'Foreign Key Field Configs'
