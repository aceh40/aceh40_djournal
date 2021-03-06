# Generated by Django 2.1.3 on 2018-12-02 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_auto_20181128_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='TennisRacket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=150)),
                ('head_size', models.IntegerField(blank=True, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('strung_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('unstrung_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('swing_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('balance', models.CharField(blank=True, max_length=20, null=True)),
                ('stiffness', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('beam_width', models.CharField(blank=True, max_length=20, null=True)),
                ('main_strings', models.IntegerField(blank=True, null=True)),
                ('cross_strings', models.IntegerField(blank=True, null=True)),
                ('min_tension', models.IntegerField(blank=True, null=True)),
                ('max_tension', models.IntegerField(blank=True, null=True)),
                ('mains_skip', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tennisstringjob',
            name='racquet_id',
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tennisstring',
            name='url',
            field=models.URLField(blank=True, help_text="Link to string's page on stringforum.net", null=True),
        ),
        migrations.AlterField(
            model_name='tennisstring',
            name='variation',
            field=models.CharField(blank=True, help_text='Enter string model variation or generation.', max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='TennisRacquet',
        ),
    ]
