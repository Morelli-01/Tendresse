# Generated by Django 4.2.2 on 2023-06-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_stats_n_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='avg_stars',
            field=models.FloatField(default=0),
        ),
    ]
