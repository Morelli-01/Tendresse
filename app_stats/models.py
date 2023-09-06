from django.db import models

# Create your models here.
class total_log(models.Model):
    count = models.IntegerField()

class ip_log(models.Model):
    ip = models.CharField(max_length=20)
    data = models.DateTimeField(auto_now=True)