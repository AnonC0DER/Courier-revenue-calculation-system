from django.dispatch import receiver
from django.db.models.signals import post_save
from income.models.DWIncome import DailyIncome, WeeklyIncome
from income.models.TripIncome import TripIncome

@receiver(post_save, sender=TripIncome)
def SaveDailyIncome(sender, instance, *args, **kwargs):
    '''Saves or updates the DailyIncome whenever a new TripIncome object is saved'''
    # If DailyIncome object is already exists
    try:
        daily_income = DailyIncome.objects.get(courier=instance.courier, date=instance.trip_date)
        daily_income.income += instance.income   
        daily_income.save()

    # If it doesn't exist
    except DailyIncome.DoesNotExist:
        DailyIncome.objects.create(courier=instance.courier, income=instance.income, date=instance.trip_date)


@receiver(post_save, sender=DailyIncome)
def SaveWeeklyIncome(sender, instance, *args, **kwargs):
    '''This signal saves and updates weekly incomes based on daily incomes'''
    # If it's saturday
    if instance.date.isoweekday() == 6:
        # If it's already exists
        try:
            weekly_income = WeeklyIncome.objects.get(courier=instance.courier, saturday=instance.date)
            weekly_income.income += instance.income
            weekly_income.save()
        
        # If it doesn't exist
        except WeeklyIncome.DoesNotExist:
            WeeklyIncome.objects.create(courier=instance.courier, income=instance.income, saturday=instance.date)