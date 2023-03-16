from django.db import models


class ForeignKeyFieldConfig(models.Model):
    on_delete = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    input_type = models.ForeignKey('InputType', on_delete=models.CASCADE, null=False, default=1)
    model_field_relation = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False, related_name='model_field_relation', default=1)
    model_field = models.ForeignKey('ModelField', on_delete=models.CASCADE, null=False, related_name='model_field')

    class Meta:
        db_table = 'ForeignKeyFieldConfig'
        verbose_name = 'Foreign Key Field Config'
        verbose_name_plural = 'Foreign Key Field Configs'
