# Generated by Django 2.2.14 on 2020-11-30 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='edad',
        ),
    ]
