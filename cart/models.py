from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.
class Product_in_Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    size = models.CharField(max_length=5, null=False )

class Cart(models.Model):
    # products = models.CharField(max_length=1000)
    validity = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, to_field='username',null=True)
    ip = models.CharField(max_length=20)
    checked_out= models.BooleanField(default=False)
    products_in_cart = models.ManyToManyField(Product_in_Cart, related_name='product_in_cart')


