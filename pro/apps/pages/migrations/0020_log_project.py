# Generated by Django 3.1.4 on 2021-01-14 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20210114_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.projectbaseinfo'),
        ),
    ]
