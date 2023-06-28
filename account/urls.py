from django.urls import path, include
from account.views import *

urlpatterns = [

    path('', account, name='account'),
    path('edit', edit_account, name='edit'),
    path('address/', add_address, name='address'),
    path('addresses/', addresses, name='addresses'),
    path('addresses/<int:id>', addresses_edit, name='addresses_edit'),
    path('addresses/delete/<int:id>', addresses_delete, name='addresses_delete'),
    path('orders/', orders, name='orders'),
    path('seller/', include('seller.urls')),
    path('feedbacks/', feedbacks, name='feedbacks')

    # path('account/addresses')
]
