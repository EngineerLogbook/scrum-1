# Generated by Django 3.0.5 on 2020-05-19 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20200516_1928'),
        ('log', '0003_auto_20200519_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.Project'),
        ),
    ]
