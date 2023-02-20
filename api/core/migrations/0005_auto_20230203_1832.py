# Generated by Django 3.2.17 on 2023-02-04 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230202_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filefieldconfig',
            name='upload_size',
        ),
        migrations.AddField(
            model_name='filefieldconfig',
            name='content_types',
            field=models.ManyToManyField(related_name='file_field_content_type_config', to='core.ContentTypes'),
        ),
        migrations.AddField(
            model_name='filefieldconfig',
            name='max_upload_size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.uploadsize'),
        ),
        migrations.AlterUniqueTogether(
            name='maintenance',
            unique_together={('user', 'project')},
        ),
    ]
