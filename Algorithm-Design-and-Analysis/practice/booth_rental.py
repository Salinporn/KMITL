def booth_rental(rental_fee, incomes):
    max_profit = 0
    for i in range(len(incomes)):
        temp_income = 0
        for j in range(i + 1, len(incomes)):
            days = j - i
            cost = rental_fee * days
            temp_income = sum(incomes[i:j])
            profit = temp_income - cost
            if profit > max_profit:
                max_profit = profit
    if max_profit <= 0:
        return "No"
    else:
        return max_profit

print(booth_rental(int(input()), [int(val) for val in input().split()]))
