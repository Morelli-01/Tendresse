from django.urls import path
from .views import *

urlpatterns = [
    path('', cart, name='cart'),
    path('atc/', atc, name='add_to_cart'),
    path('remove/', rfc, name='remove_from_cart'),
    path('items/count/', get_n_items, name='get_n_items'),
]
