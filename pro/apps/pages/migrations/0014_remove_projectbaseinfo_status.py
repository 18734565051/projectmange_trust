# Generated by Django 3.1.4 on 2021-01-11 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20210111_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectbaseinfo',
            name='status',
        ),
    ]
