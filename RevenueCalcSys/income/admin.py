from django.contrib import admin
from income.models.TripIncome import TripIncome

class TripIncomeAdmin(admin.ModelAdmin):
    list_display = ['courier', 'income', 'trip_date']
    search_fields = ['courier__full_name', 'trip_date']
    readonly_fields = ['trip_date']
    

admin.site.register(TripIncome, TripIncomeAdmin)