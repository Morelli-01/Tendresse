import json

from django.contrib.auth.models import User

from django.test import TestCase


class AddProductToCartViewsTest(TestCase):
    # def setUp(self) -> None:
    #     user = User.objects.create_superuser("nicola", "nicolamorelli@jemore.it", "sudo")
    #     user.save()

    def test_atc(self):
        for p in self.client.get('/product/').context['products']:
            # print(p.pid)
            payload = json.dumps({
                'pid': str(p.pid),
                'qty': '1',
                'size': 'S'
            })
            self.assertEqual(self.client.post('/cart/atc/', content_type='application/json', data=payload).status_code,
                             201)

    def test_atc_exceed_qty(self):
        for p in self.client.get('/product/').context['products']:
            # print(p.pid)
            payload = json.dumps({
                'pid': str(p.pid),
                'qty': '101',
                'size': 'S'
            })
            self.assertEqual(self.client.post('/cart/atc/', content_type='application/json', data=payload).status_code,
                             406)
