from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Cart(models.Model):
    products = models.CharField(max_length=1000)
    validity = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, to_field='username',null=True)
    ip = models.CharField(max_length=20)
    checked_out= models.BooleanField(default=False)


