from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from account.models import Address
from cart.models import Cart


def validate_float(value):
    # Converti il valore in stringa e rimuovi gli spazi iniziali e finali
    value_str = str(value).strip()

    # Controlla il numero di cifre nel valore
    if len(value_str) > 5:
        raise ValidationError('Il numero di cifre non deve superare 5.')


# Create your models here.
class Checkout(models.Model):
    ship_method = models.CharField(max_length=20)
    addr = models.ForeignKey(Address, on_delete=models.DO_NOTHING, to_field='id')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, to_field='id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', null=True)
    payment_method = models.CharField(max_length=20)
    confirmed = models.BooleanField(default=False)
    total_price = models.FloatField(default=0, validators=[validate_float])

