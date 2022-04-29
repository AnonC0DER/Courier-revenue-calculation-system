from rest_framework import serializers
from income.models.DWIncome import WeeklyIncome

class WeeklyIncomeSerializer(serializers.ModelSerializer):
    '''Serializes the weekly income'''
    class Meta:
        model = WeeklyIncome
        depth = 2
        fields = '__all__'