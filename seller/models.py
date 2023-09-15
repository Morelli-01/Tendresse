from django.db import models

from account.models import Feedback
from cart.models import Cart
from checkout.models import Checkout
from product.models import Product


# Create your models here.
class Stats(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, )
    n_sales = models.IntegerField(default=0)
    avg_stars = models.FloatField(default=0)
    n_feedback = models.IntegerField(default=0)

    def calc_stats(self):
        # self.n_sales = Cart.objects.all().filter(products__contains=self.product.pid, checked_out=True).count()
        self.n_sales = Cart.objects.all().filter(products_in_cart__product__pid =self.product.pid, checked_out=True).count()

    def calc_avg_stars(self):
        feeds = Feedback.objects.all().filter(product=self.product)
        sum = 0
        for f in feeds:
            sum += f.stars
        if feeds.count() != 0:
            self.avg_stars = float(str((sum / feeds.count()))[:3])

    def calc_feedback(self ):
        self.n_feedback = Feedback.objects.all().filter(product=self.product).count()