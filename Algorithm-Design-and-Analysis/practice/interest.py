def optimal_interest(number1, number2, number3):
    max_profit = 0.0
    interest = 0.0
    temp_interest = 0.0
    while temp_interest <= 20:
        profit = (
            number1 * (temp_interest ** 3) +
            number2 * (temp_interest ** 2) +
            number3 * temp_interest
            )
        if profit > max_profit:
            max_profit = profit
            interest = temp_interest
        temp_interest = round(temp_interest + 0.01, 2)
    return str(interest)

print(optimal_interest(float(input()), float(input()), float(input())))
