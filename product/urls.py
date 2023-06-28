from django.urls import path
from .views import *


urlpatterns = [
    path('', products, name='product_home'),
    path('ordered/<str:type>', products_ordered, name='product_ordered'),
    path('<str:pid>', product, name='product_home'),

]
