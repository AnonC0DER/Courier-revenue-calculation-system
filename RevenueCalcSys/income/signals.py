from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from income.models.DWIncome import DailyIncome, WeeklyIncome
from income.models.TripIncome import TripIncome, DecreaseIncome, IncreaseIncome

@receiver(post_save, sender=TripIncome)
def SaveDailyIncome(sender, instance, *args, **kwargs):
    '''Saves or updates the DailyIncome whenever a new TripIncome object is saved'''
    # If there's IncreaseIncome
    try:
        increase_income = IncreaseIncome.objects.get(courier=instance.courier, date=instance.trip_date)
        instance.income += increase_income.amount

        # Delete the increase_income
        increase_income.delete()

    except IncreaseIncome.DoesNotExist:
        pass

    # If there's DecreaseIncome
    try:
        decrease_income = DecreaseIncome.objects.get(courier=instance.courier)
        instance.income -= decrease_income.amount

        if instance.income <= 0:
            instance.income = 0
        
        # Delete the decrease_income
        decrease_income.delete()

    except DecreaseIncome.DoesNotExist:
        pass
    
    # If DailyIncome object is already exists
    try:
        daily_income = DailyIncome.objects.get(courier=instance.courier, date=instance.trip_date)
        daily_income.income += instance.income   
        daily_income.save()

    # If it doesn't exist
    except DailyIncome.DoesNotExist:
        DailyIncome.objects.create(courier=instance.courier, income=instance.income, date=instance.trip_date)


@receiver(post_save, sender=TripIncome)
def SaveWeeklyIncome(sender, instance, *args, **kwargs):
    '''This signal saves and updates weekly incomes based on daily incomes'''
    # If it's saturday
    if instance.trip_date.isoweekday() == 6:
        # If it's already exists
        try:
            weekly_income = WeeklyIncome.objects.get(courier=instance.courier, saturday=instance.trip_date)
            weekly_income.income += instance.income
            weekly_income.save()
        
        # If it doesn't exist
        except WeeklyIncome.DoesNotExist:
            WeeklyIncome.objects.create(courier=instance.courier, income=instance.income, saturday=instance.trip_date)

    # If it's not saturday
    else:
        try:
            # Increases the latest saturday income
            weekly_income = WeeklyIncome.objects.filter(courier=instance.courier).latest('saturday')
            weekly_income.income += instance.income
            weekly_income.save()

        except WeeklyIncome.DoesNotExist:
            WeeklyIncome.objects.create(courier=instance.courier, income=instance.income, saturday=instance.trip_date)