# Generated by Django 2.1.3 on 2018-11-18 23:51

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Weight in lb')),
                ('note', models.TextField()),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 18, 23, 51, 21, 901563, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 18, 23, 51, 21, 870363, tzinfo=utc)),
        ),
    ]
