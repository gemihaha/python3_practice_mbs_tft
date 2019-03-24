food = 157.50
#total_cost = float(total_cost)
tax = food * 0.08875
service_fee = (food + tax) * 0.15

print('The total cost is {:.2f}' .format(food + tax + service_fee))
