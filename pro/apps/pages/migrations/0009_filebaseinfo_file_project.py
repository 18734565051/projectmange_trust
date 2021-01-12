# Generated by Django 3.1.4 on 2021-01-04 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_filebaseinfo_is_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='filebaseinfo',
            name='file_project',
            field=models.ForeignKey(help_text='项目阶段', null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.projectbaseinfo', verbose_name='文档隶属项目阶段'),
        ),
    ]