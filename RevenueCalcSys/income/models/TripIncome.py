from django.db import models
from courier.models import Courier

class TripIncome(models.Model):
    '''This model saves trip income for each trip'''
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    # income cannot be negative
    income = models.PositiveIntegerField()
    trip_date = models.DateField(auto_created=True)


class IncreaseIncome(models.Model):
    '''This model increase incomes based on out-of-shift and area trips'''
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    descriptions = models.TextField()
    date = models.DateField(auto_created=True)


class DecreaseIncome(models.Model):
    '''This model decrease incomes based on damages, frauds, refusal to travel etc.'''
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    descriptions = models.TextField()
    date = models.DateField(auto_created=True)