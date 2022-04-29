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
    
    def test_DailyIncome_increases_by_IncreaseIncome(self):
        '''Test DailyIncome object increases by IncreaseIncome object'''
        increase_income = IncreaseIncome.objects.create(courier=self.courier, amount=50, descriptions='Birthday gift', date=date(2022, 4, 29))
        trip_1 = TripIncome.objects.create(courier=self.courier, income=100, trip_date=date(2022, 4, 29))
        daily_income = DailyIncome.objects.get(courier=self.courier, date=date(2022, 4, 29))
        
        self.assertEqual(daily_income.income, 150)
    
    def test_DailyIncome_decreases_by_DecreaseIncome(self):
        '''Test DailyIncome object decrease by DecreaseIncome object'''
        decrease_income = DecreaseIncome.objects.create(courier=self.courier, amount=25, descriptions='Damage', date=date(2022, 4, 29))
        trip_1 = TripIncome.objects.create(courier=self.courier, income=100, trip_date=date(2022, 4, 29))
        daily_income = DailyIncome.objects.get(courier=self.courier, date=date(2022, 4, 29))

        self.assertEqual(daily_income.income, 75)

    def test_DailyIncome_increases_and_decreases(self):
        '''Test DailyIncome object increases and decrease by DecreaseIncome and IncreaseIncome'''
        increase_income = IncreaseIncome.objects.create(courier=self.courier, amount=50, descriptions='Birthday gift', date=date(2022, 4, 29))
        decrease_income = DecreaseIncome.objects.create(courier=self.courier, amount=25, descriptions='Damage', date=date(2022, 4, 29))
        trip = TripIncome.objects.create(courier=self.courier, income=100, trip_date=date(2022, 4, 29))
        daily_income = DailyIncome.objects.get(courier=self.courier, date=date(2022, 4, 29))

        self.assertEqual(daily_income.income, 125)


class TestWeeklyIncome(TestCase):
    '''Tests to test WeeklyIncome'''

    def setUp(self):
        self.courier = Courier.objects.create(full_name='Test Courier')
        # Create 8 TripIncome in 8 days
        self.sample_TripIncome(29, 4)
        self.sample_TripIncome(30, 4)
        self.sample_TripIncome(1, 5)
        self.sample_TripIncome(2, 5)
        self.sample_TripIncome(3, 5)
        self.sample_TripIncome(4, 5)
        self.sample_TripIncome(5, 5)
        self.sample_TripIncome(6, 5)

    def sample_TripIncome(self, day, month):
        '''Creates a sample TripIncome object'''
        TripIncome.objects.create(courier=self.courier, income=100, trip_date=date(2022, month, day))

    def test_WeeklyIncome_objects(self):
        '''Test WeeklyIncome objects'''
        qs = WeeklyIncome.objects.all()
        
        self.assertEqual(qs.count(), 2)
        self.assertEqual(qs.first().income, 100)
        self.assertEqual(qs.get(id=2).income, 700)