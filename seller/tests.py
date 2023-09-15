from django.contrib.auth.models import User

from django.test import TestCase



class AddProductViewsTest(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_superuser("nicola", "nicolamorelli@jemore.it", "sudo")
        user.save()

    def test_product_creation(self):
        self.client.login(username='nicola', password='sudo')

        self.assertEqual(self.client.post('/account/seller/',
                                          {'image': 'product1.webp', 'title': 'prodotto di prova', 'price': '35',
                                           'description': 'Maglia viola', 'size-xs': '1', 'size-s': '1', 'size-m': '1',
                                           'size-l': '1', 'size-xl': '1', 'cat-tag': 'Maglia',
                                           'col-tag': 'Viola'}).status_code, 200)
    def test_product_creation_with_missing_fields(self):
        self.client.login(username='nicola', password='sudo')

        self.assertEqual(self.client.post('/account/seller/',
                               {'image': 'product1.webp', 'title': 'prodotto di prova',
                                # 'price': '35',
                                'description': 'Maglia viola', 'size-xs': '1', 'size-s': '1', 'size-m': '1',
                                'size-l': '1', 'size-xl': '1','cat-tag':'Maglia', 'col-tag':'Viola' }).status_code, 302)

