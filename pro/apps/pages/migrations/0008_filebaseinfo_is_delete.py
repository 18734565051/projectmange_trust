# Generated by Django 3.1.4 on 2020-12-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_filebaseinfo_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='filebaseinfo',
            name='is_delete',
            field=models.BooleanField(default=0, help_text='是否删除', verbose_name='是否删除'),
        ),
    ]
