from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)


class Product(models.Model):
    title = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0, null=False)
    img1 = models.CharField(max_length=100, null=False)
    img2 = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    available_sizes = models.TextField(max_length=100, null=False)
    pid = models.AutoField(primary_key=True, db_column='pid')
    category_tags = models.ManyToManyField(Tag, related_name='products_with_category_tags')
    color_tags = models.ManyToManyField(Tag, related_name='products_with_color_tags')
    for_sale = models.BooleanField(default=True)
