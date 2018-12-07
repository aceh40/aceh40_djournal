# Generated by Django 2.1.3 on 2018-11-28 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20181118_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='TennisRacquet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('variation', models.CharField(max_length=100)),
                ('head_size', models.IntegerField()),
                ('length', models.DecimalField(decimal_places=2, max_digits=4)),
                ('strung_weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('unstrung_weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('swing_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('balance', models.CharField(max_length=20)),
                ('stiffness', models.DecimalField(decimal_places=2, max_digits=5)),
                ('beam_width', models.CharField(max_length=20)),
                ('main_strings', models.IntegerField()),
                ('cross_strings', models.IntegerField()),
                ('min_tension', models.IntegerField()),
                ('max_tension', models.IntegerField()),
                ('mains_skip', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TennisString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(help_text='Enter string maker.', max_length=20)),
                ('model', models.CharField(help_text='Enter string model.', max_length=20)),
                ('variation', models.CharField(help_text='Enter string model variation or generation.', max_length=100)),
                ('type', models.CharField(choices=[('g', 'Natural Gut'), ('p', 'Polyester'), ('m', 'Multifilament'), ('n', 'Nylon')], help_text='Type of string', max_length=1)),
                ('gauge', models.CharField(choices=[('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19')], help_text='Gauge of string', max_length=2)),
                ('url', models.URLField(help_text="Link to string's page on stringforum.net")),
            ],
        ),
        migrations.CreateModel(
            name='TennisStringJob',
            fields=[
                ('journalentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.JournalEntry')),
                ('main_tension', models.DecimalField(decimal_places=1, max_digits=3)),
                ('cross_tension', models.DecimalField(decimal_places=1, max_digits=3)),
                ('cross_string_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cross_string_id', to='journal.TennisString')),
                ('main_string_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_string_id', to='journal.TennisString')),
                ('racquet_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journal.TennisRacquet')),
            ],
            bases=('journal.journalentry',),
        ),
        migrations.AlterModelOptions(
            name='journalentry',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='weightentry',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='weightentry',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]