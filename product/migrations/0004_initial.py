# Generated by Django 4.1.7 on 2023-06-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_delete_product_sm_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_sm',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('img1', models.CharField(max_length=100)),
                ('img2', models.CharField(max_length=100)),
                ('pid', models.AutoField(db_column='pid', primary_key=True, serialize=False)),
            ],
        ),
    ]
