# Generated by Django 4.2.2 on 2023-08-10 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_in_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validity', models.DateTimeField(null=True)),
                ('ip', models.CharField(max_length=20)),
                ('checked_out', models.BooleanField(default=False)),
                ('products_in_cart', models.ManyToManyField(related_name='product_in_cart', to='cart.product_in_cart')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
