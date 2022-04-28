from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from income.models.DWIncome import DailyIncome
from income.models.TripIncome import TripIncome

@receiver(post_save, sender=TripIncome)
def SaveDailyIncome(sender, instance, *args, **kwargs):
    '''Saves or updates the DailyIncome whenever a new TripIncome object is saved'''
    # If DailyIncome object is already exists
    try:
        daily_income = DailyIncome.objects.get(courier=instance.courier, date=instance.trip_date)
        daily_income.income += instance.income   
        daily_income.save()

    except DailyIncome.DoesNotExist:
        DailyIncome.objects.create(courier=instance.courier, income=instance.income, date=instance.trip_date)