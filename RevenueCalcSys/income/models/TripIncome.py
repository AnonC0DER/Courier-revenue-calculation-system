from django.db import models
from courier.models import Courier

class TripIncome(models.Model):
    '''This model saves trip income for each trip'''
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    # income cannot be negative
    income = models.PositiveIntegerField()
    trip_date = models.DateField(auto_now_add=True)