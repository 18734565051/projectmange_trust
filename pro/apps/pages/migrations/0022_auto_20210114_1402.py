# Generated by Django 3.1.4 on 2021-01-14 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_log_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='filebaseinfo',
            name='project_status',
            field=models.CharField(help_text='文档隶属项目状态', max_length=50, null=True, verbose_name='文档隶属项目状态'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='file_project',
            field=models.ForeignKey(help_text='隶属项目', null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.projectbaseinfo', verbose_name='隶属项目'),
        ),
    ]