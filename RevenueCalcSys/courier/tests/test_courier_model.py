from django.test import TestCase
from courier.models import Courier

class TestCourierModel(TestCase):
    '''Tests to test courier model'''

    def test_create_new_courier(self):
        '''Test creating a new courier is successful'''
        courier = Courier.objects.create(full_name='Test Courier')
        qs = Courier.objects.first()

        self.assertEqual(courier.id, qs.id)

    def test_uuid_unique(self):
        '''Test creating couriers using UUID instead of primary key is unique'''
        courier = Courier.objects.create(full_name='Test Courier')
        courier2 = Courier.objects.create(full_name='Test Courier 2')
        
        self.assertNotEqual(courier.id, courier2.id)