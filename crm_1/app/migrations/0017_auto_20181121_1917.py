# Generated by Django 2.1.1 on 2018-11-21 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20181121_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='app.Group'),
        ),
    ]
