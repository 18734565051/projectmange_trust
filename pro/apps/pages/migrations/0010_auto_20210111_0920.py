# Generated by Django 3.1.4 on 2021-01-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_filebaseinfo_file_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filebaseinfo',
            name='file_router',
            field=models.FileField(help_text='文件存储路径', upload_to='Files/%Y/%m/%d/', verbose_name='文件存储路径'),
        ),
    ]