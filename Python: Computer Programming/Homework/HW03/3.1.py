name = input("Enter employee's name: ")
hour = float(input("Enter number of hours worked in a week: "))
pay = float(input("Enter hourly pay rate: "))
f_tax = float(input("Enter federal tax withholding rate: "))
s_tax = float(input("Enter state tax withholding rate: "))


def rounddown(x, dec):
    y = 1 / (10 ** dec)
    return (x // y) * y


gross = hour * pay
fed = gross * f_tax
sta = gross * s_tax
net = rounddown(gross - fed - sta, 2)

fede = round(fed, 2)
stat = rounddown(sta, 2)
total = fede + stat

print(f"Employee Name: {name}\nHours Worked: {hour}\nPay Rate: ${pay}\n"
      f"Gross Pay: {gross}\nDeductions:\n   Federal Withholding "
      f"({f_tax*100}%) : ${fede}\n   State Withholding ({s_tax*100}%) "
      f": ${stat}\n   Total Deduction : ${total}\nNet Pay : ${net}")
