# Generated by Django 3.1.4 on 2020-12-23 02:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_projectbaseinfo_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectbaseinfo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='项目编号', primary_key=True, serialize=False, verbose_name='项目编号'),
        ),
    ]
