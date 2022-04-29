from django.contrib import admin
from income.models.TripIncome import TripIncome, IncreaseIncome, DecreaseIncome
from income.models.DWIncome import DailyIncome, WeeklyIncome


class TripIncomeAdmin(admin.ModelAdmin):
    list_display = ['courier', 'income', 'trip_date']
    search_fields = ['courier__full_name', 'trip_date']


class IncreaseDecreaseIncomeAdmin(admin.ModelAdmin):
    list_display = ['courier', 'amount', 'date']
    search_fields = ['courier__full_name', 'date']


class DailyIncomeAdmin(admin.ModelAdmin):
    list_display = ['courier', 'income', 'date']
    search_fields = ['courier__full_name', 'date']


class WeeklyIncomeAdmin(admin.ModelAdmin):
    list_display = ['courier', 'saturday', 'income']
    search_fields = ['courier__full_name', 'saturday']


admin.site.register(TripIncome, TripIncomeAdmin)
admin.site.register(IncreaseIncome, IncreaseDecreaseIncomeAdmin)
admin.site.register(DecreaseIncome, IncreaseDecreaseIncomeAdmin)
admin.site.register(WeeklyIncome, WeeklyIncomeAdmin)
admin.site.register(DailyIncome, DailyIncomeAdmin)