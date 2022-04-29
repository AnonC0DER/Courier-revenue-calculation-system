from django.test import TestCase
from datetime import date
from income.models.TripIncome import TripIncome, IncreaseIncome, DecreaseIncome
from income.models.DWIncome import DailyIncome, WeeklyIncome
from courier.models import Courier

class TestDailyIncome(TestCase):
    '''Tests to test daily income model its signals'''
    def setUp(self):
        self.courier = Courier.objects.create(full_name='Test Courier')

    def test_DailyIncome_increases_by_TripIncome(self):
        '''Test DailyIncome object increases by each TripIncome object'''
        trip_1 = TripIncome.objects.create(courier=self.courier, income=35, trip_date=date(2022, 4, 29))
        trip_2 = TripIncome.objects.create(courier=self.courier, income=50, trip_date=date(2022, 4, 29))
        daily_income = DailyIncome.objects.get(courier=self.courier, date=date(2022, 4, 29))
        trip_3 = TripIncome.objects.create(courier=self.courier, income=80, trip_date=date(2022, 4, 30))
        daily_income_2 = DailyIncome.objects.get(courier=self.courier, date=trip_3.trip_date)

        self.assertEqual(trip_1.income + trip_2.income, daily_income.income)
        self.assertEqual(trip_3.income, daily_income_2.income)
        self.assertEqual(DailyIncome.objects.all().count(), 2)
        self.assertEqual(TripIncome.objects.all().count(), 3)