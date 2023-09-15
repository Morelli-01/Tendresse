# Generated by Django 4.2.2 on 2023-08-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('img1', models.CharField(max_length=100)),
                ('img2', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('available_sizes', models.TextField(max_length=100)),
                ('pid', models.AutoField(db_column='pid', primary_key=True, serialize=False)),
                ('for_sale', models.BooleanField(default=True)),
                ('category_tags', models.ManyToManyField(related_name='products_with_category_tags', to='product.tag')),
                ('color_tags', models.ManyToManyField(related_name='products_with_color_tags', to='product.tag')),
            ],
        ),
    ]
