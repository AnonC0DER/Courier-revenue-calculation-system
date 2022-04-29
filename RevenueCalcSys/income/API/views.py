from rest_framework.generics import ListAPIView
from income.API.serializers import WeeklyIncomeSerializer
from income.models.DWIncome import WeeklyIncome

class WeeklyIncomeView(ListAPIView):
    serializer_class = WeeklyIncomeSerializer
    
    def get_queryset(self):
        '''from_date and to_date queries'''
        # url : /api/weekly-incomes/?from_date=0000-00-00
        from_date = self.request.query_params.get('from_date')
        # url : /api/weekly-incomes/?to_date=0000-00-00
        to_date = self.request.query_params.get('to_date')
        queryset = WeeklyIncome.objects.all()
        if from_date:
            # saturday date greater than or equals to from_date
            queryset = WeeklyIncome.objects.filter(saturday__gte=from_date)        
        
        if to_date:
            # saturday date less than or equals to to_date
            queryset = WeeklyIncome.objects.filter(saturday__lte=to_date)

        return queryset