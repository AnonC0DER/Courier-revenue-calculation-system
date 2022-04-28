from django.contrib import admin
from income.models.TripIncome import TripIncome, IncreaseIncome, DecreaseIncome

class TripIncomeAdmin(admin.ModelAdmin):
    list_display = ['courier', 'income', 'trip_date']
    search_fields = ['courier__full_name', 'trip_date']
    readonly_fields = ['trip_date']


class IncreaseDecreaseIncomeAdmin(admin.ModelAdmin):
    list_display = ['courier', 'amount', 'date']
    search_fields = ['courier__full_name', 'date']
    readonly_fields = ['date']


admin.site.register(TripIncome, TripIncomeAdmin)
admin.site.register(IncreaseIncome, IncreaseDecreaseIncomeAdmin)
admin.site.register(DecreaseIncome, IncreaseDecreaseIncomeAdmin)