# Generated by Django 4.2.2 on 2023-06-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_tag_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='category_tags',
            field=models.ManyToManyField(to='product.tag'),
        ),
    ]
