# Generated by Django 2.1.3 on 2018-12-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0018_auto_20181211_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstatusref',
            name='logical_order',
            field=models.IntegerField(unique=True),
        ),
    ]
