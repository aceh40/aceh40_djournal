# Generated by Django 2.1.3 on 2018-12-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0014_auto_20181211_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstatusref',
            name='logical_order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]