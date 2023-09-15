from django.db import models

# Create your models here.
class bolle_old(models.Model):
    numero = models.IntegerField(null=False)
    anno = models.IntegerField(null=False)


    class Meta:
        unique_together = ('numero', 'anno')

