from django.urls import path
from income.API import views

urlpatterns = [
    path('weekly-incomes/', views.WeeklyIncomeView.as_view(), name='weekly-incomes')
]