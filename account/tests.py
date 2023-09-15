from django.test import TestCase

# Create your tests here.
import json

from django.contrib.auth.models import User

from django.test import TestCase

from checkout.models import Checkout


class FeedbackViewsTest(TestCase):
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
        addr_id = (self.client.get('/account/addresses/').context['addresses'][0].id)

        self.client.post('/checkout/1/', content_type='application/json',
                         data=json.dumps({'addr_id': addr_id, 'ship_method': 'collect'}))

        self.client.post('/checkout/2/', content_type='application/json',
                         data=json.dumps({'payment_method': 'collect'}))

    def test_valid_feedback(self):
        p = self.client.get('/product/').context['products'][0]
        self.assertEqual(self.client.post('/account/orders/', {'pid-input': str(p.pid),
                                                    'star-count': 5,
                                                    'comment': 'test comment'}).status_code, 200)


    def test_invalid_feedback(self):
        p = self.client.get('/product/').context['products'][1]
        self.assertEqual(self.client.post('/account/orders/', {'pid-input': str(p.pid),
                                                    'star-count': 5,
                                                    'comment': 'test comment'}).status_code, 400)

