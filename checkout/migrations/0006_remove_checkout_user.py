# Generated by Django 4.2.2 on 2023-06-29 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_checkout_addr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='user',
        ),
    ]
