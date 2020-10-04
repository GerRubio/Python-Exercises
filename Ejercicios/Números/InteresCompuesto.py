INTERESTS = 4

money_quantity = float(input('Amount of money: '))

first_year_interest = money_quantity * (INTERESTS / 100) + money_quantity
second_year_interest = first_year_interest * (INTERESTS / 100) + first_year_interest
third_year_interest = second_year_interest * (INTERESTS / 100) + second_year_interest

print('First year interests: ', round(first_year_interest), 3)
print('Second year interests: ', round(second_year_interest), 3)
print('Third year interests: ', round(third_year_interest), 3)