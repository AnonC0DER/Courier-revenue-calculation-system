# Courier revenue calculation system

## Miare.ir Techical task
Read [TODO list](https://github.com/AnonC0DER/Courier-revenue-calculation-system/blob/main/TODO.md)

## Unsolved problems
- [ ] There's one unsolved problem in [signals](https://github.com/AnonC0DER/Courier-revenue-calculation-system/blob/main/RevenueCalcSys/income/signals.py#L36)

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
