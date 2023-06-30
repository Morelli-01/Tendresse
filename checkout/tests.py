import json

from django.contrib.auth.models import User

from django.test import TestCase


class CollectViewsTest(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user("nicola", "nicolamorelli@jemore.it", "sudo")
        user.save()
        self.client.login(username='nicola', password='sudo')
        p = self.client.get('/product/').context['products'][0]

        payload = json.dumps({
            'pid': str(p.pid),
            'qty': '1',
            'size': 'S'
        })
        self.client.post('/cart/atc/', content_type='application/json', data=payload)
        self.client.post('/account/address/',
                         {'name': 'Nicola', 'surname': 'Morelli', 'line1': 'Via Giacomo Puccini 22',
                          'city': 'Carpi', 'province': 'MO', 'zip': '41012', 'line2': ''})

    def test_collect_shipment_collect_payment(self):

        addr_id = (self.client.get('/account/addresses/').context['addresses'][0].id)

        self.assertEqual(self.client.post('/checkout/1/', content_type='application/json',
                         data=json.dumps({'addr_id': addr_id, 'ship_method': 'collect'})).status_code,200)
        self.assertEqual(self.client.post('/checkout/2/', content_type='application/json',
                         data=json.dumps({'payment_method': 'collect'})).status_code, 201)

    def test_standard_shipment_collect_payment(self):

        addr_id = (self.client.get('/account/addresses/').context['addresses'][0].id)

        self.assertEqual(self.client.post('/checkout/1/', content_type='application/json',
                         data=json.dumps({'addr_id': addr_id, 'ship_method': 'standard'})).status_code,200)
        self.assertEqual(self.client.post('/checkout/2/', content_type='application/json',
                         data=json.dumps({'payment_method': 'collect'})).status_code, 409)
