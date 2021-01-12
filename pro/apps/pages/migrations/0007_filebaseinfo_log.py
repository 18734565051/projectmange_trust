# Generated by Django 3.1.4 on 2020-12-29 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0006_auto_20201223_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.IntegerField(help_text='id', primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.CharField(help_text='用户名', max_length=20, verbose_name='用户名')),
                ('content', models.TextField(help_text='内容', verbose_name='内容')),
            ],
            options={
                'verbose_name': '日志表',
                'verbose_name_plural': '日志表',
                'db_table': 'tb_log',
            },
        ),
        migrations.CreateModel(
            name='FileBaseInfo',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='文档编号', primary_key=True, serialize=False, verbose_name='文档编号')),
                ('name', models.CharField(help_text='文档名字', max_length=50, verbose_name='文件名称')),
                ('trial_status', models.CharField(help_text='未审核、已审核、正在审核', max_length=20, verbose_name='审核状态')),
                ('file_router', models.CharField(help_text='文件存储路径', max_length=200, verbose_name='文件存储路径')),
                ('founder', models.ForeignKey(help_text='创建人', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '文档基本信息表',
                'verbose_name_plural': '文档基本信息表',
                'db_table': 'tb_filebaseInfo',
            },
        ),
    ]
