from django.db import models
from django.contrib.auth.models import User

from product.models import Product


# Create your models here.

class Address(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')

class Feedback(models.Model):
    product = models.ForeignKey(Product, to_field='pid', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    stars = models.IntegerField()
    comment = models.CharField(max_length=250)

    class Meta:
        unique_together = ('user', 'product')

