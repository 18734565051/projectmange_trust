# Generated by Django 3.1.4 on 2021-01-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approval', '0003_auto_20210120_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowmodel',
            name='flow_no',
            field=models.CharField(default='f364926', help_text='流程号', max_length=200, verbose_name='流程号'),
        ),
    ]
