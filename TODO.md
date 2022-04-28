### Courier revenue calculation system

- Must be done using Django rest framework
- Queries must be optimized
- Consistency is important
- Use tests to test calculation of daily income table


## Couriers' income
    
- Earnings :
    - Distance, customer type, time, distance, etc.
    - It can't be negative

- Increase revenue :
    - It's not related to earnings
    - Income out-of-shift / area trips

-  Deduction of income :
    - It's not related to earnings
    - Damages, frauds, refusal to travel


## Weekly income

- A table :
    - First day of week date
    - Total daily income 
    - This model is an aggregate of daily income model.

- A view :
    - Results : 
        - Courier name
        - Dates (First day of week (from_date, to_date))
        - For each of these rows, serialize the courier **name**.