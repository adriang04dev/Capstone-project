from django.test import TestCase
from Restaurant.models import *

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = menu.objects.create(title='first', price='1.00')
        self.item2 = menu.objects.create(title='second', price='2.00')

    def test_getall(self):
        first = menu.objects.get(title='first')
        second = menu.objects.get(title='second')

        self.assertEqual(str(first), 'first : 1.00')
        self.assertEqual(str(second), 'second : 2.00')