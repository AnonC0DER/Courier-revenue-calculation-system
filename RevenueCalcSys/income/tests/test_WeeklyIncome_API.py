from django.test import TestCase
from rest_framework.test import APIClient
from datetime import date
from courier.models import Courier
from income.models.DWIncome import WeeklyIncome


class TestWeeklyIncomeAPI(TestCase):
    '''Tests to test WeeklyIncome API'''
    def setUp(self):
        self.client = APIClient()
        self.courier_1 = Courier.objects.create(full_name='Test Courier')
        self.courier_2 = Courier.objects.create(full_name='Test Courier 2')
        self.weekly_income = WeeklyIncome.objects.create(courier=self.courier_1, saturday=date(2022, 4, 2), income=120)
        self.weekly_income2 = WeeklyIncome.objects.create(courier=self.courier_2, saturday=date(2022, 4, 9), income=500)
        self.weekly_income3 = WeeklyIncome.objects.create(courier=self.courier_1, saturday=date(2022, 4, 16), income=320)

    def test_get_WeeklyIncome_list(self):
        '''Test WeeklyIncome list view'''
        res = self.client.get('/api/weekly-incomes/').json()
        
        self.assertEqual(len(res), 3)
        self.assertEqual(self.weekly_income.income, res[0]['income'])
        self.assertEqual(str(self.weekly_income3.courier.id), res[2]['courier']['id'])

    def test_WeeklyIncome_from_date(self):
        '''Test WeeklyIncome from_date queryset'''
        res = self.client.get('/api/weekly-incomes/?from_date=2022-04-3').json()
        
        self.assertEqual(len(res), 2)
        self.assertEqual(str(self.weekly_income2.courier.id), res[0]['courier']['id'])
    
    def test_WeeklyIncome_to_date(self):
        '''Test WeeklyIncome to_date queryset'''
        res = self.client.get('/api/weekly-incomes/?to_date=2022-04-3').json()
        
        self.assertEqual(len(res), 1)
        self.assertEqual(str(self.weekly_income.courier.id), res[0]['courier']['id'])