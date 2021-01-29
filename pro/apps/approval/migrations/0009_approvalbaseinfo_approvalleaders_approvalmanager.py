# Generated by Django 3.1.4 on 2021-01-27 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('approval', '0008_auto_20210127_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(help_text='备注', null=True, verbose_name='备注')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '审批管理员表',
                'verbose_name_plural': '审批管理员表',
                'db_table': 'tb_approvalmanager',
            },
        ),
        migrations.CreateModel(
            name='ApprovalLeaders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(help_text='备注', null=True, verbose_name='负责人备注')),
                ('leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='approval.approvalmanager')),
            ],
            options={
                'verbose_name': '审批负责人表',
                'verbose_name_plural': '审批负责人表',
                'db_table': 'tb_ApprovalLeaders',
            },
        ),
        migrations.CreateModel(
            name='ApprovalBaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manger', models.BooleanField(default=0, help_text='是否需要管理员审批', verbose_name='是否需要管理员审批')),
                ('leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='approval.approvalleaders')),
                ('task', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='approval.task', verbose_name='任务审核')),
            ],
            options={
                'verbose_name': '审批基本信息表',
                'verbose_name_plural': '审批基本信息表',
                'db_table': 'tb_approvalbaseinfo',
            },
        ),
    ]
