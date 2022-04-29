# Courier revenue calculation system

## Read [TODO list](https://github.com/AnonC0DER/Courier-revenue-calculation-system/blob/main/TODO.md)

## Unsolved problems
- [x] Unsolved problem successfully [solved](https://github.com/AnonC0DER/Courier-revenue-calculation-system/commit/83e650f7ccbba3bb3924d6d616bb990203b1de45)

## Setup
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py test`


## Files
- [WeeklyIncome API](https://github.com/AnonC0DER/Courier-revenue-calculation-system/tree/main/RevenueCalcSys/income/API)
- [Courier model](https://github.com/AnonC0DER/Courier-revenue-calculation-system/blob/main/RevenueCalcSys/courier/models.py)
- [DailyIncome and WeeklyIncome models](https://github.com/AnonC0DER/Courier-revenue-calculation-system/blob/main/RevenueCalcSys/income/models/DWIncome.py)
- [TripIncome, IncreaseIncome and DecreaseIncome models](https://github.com/AnonC0DER/Courier-revenue-calculation-system/blob/main/RevenueCalcSys/income/models/TripIncome.py)
- [All signals](https://github.com/AnonC0DER/Courier-revenue-calculation-system/blob/main/RevenueCalcSys/income/signals.py)
- [Income app tests](https://github.com/AnonC0DER/Courier-revenue-calculation-system/tree/main/RevenueCalcSys/income/tests)
- [Courier app tests](https://github.com/AnonC0DER/Courier-revenue-calculation-system/tree/main/RevenueCalcSys/courier/tests)
