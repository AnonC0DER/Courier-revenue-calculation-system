from django.db import models
from courier.models import Courier

class DailyIncome(models.Model):
    '''This model saves daily income for each courier'''
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    income = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)


class WeeklyIncome(models.Model):
    '''This model saves weekly income for each courier'''
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    saturday = models.DateField(help_text='Put date of first day of the week')
    income = models.PositiveIntegerField()