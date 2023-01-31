from django.db import models


class Maintenance(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Maintenance'
        verbose_name = 'Maintenance'
        verbose_name_plural = 'Maintenances'

    def __str__(self):
        return f'{self.user.name} {self.user.last_name} - {self.project.name}'
