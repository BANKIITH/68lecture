keep_going = 'y'

while keep_going.lower() == 'y':
    sales = float(input("Enter the amount of sales: "))
    comm_rates = float(input("Enter the commission rate: "))

    commission = sales * comm_rates
    print(f"the commission is ${commission:.2f}")
    keep_going = (input('if you want to calcurate another' + \
                        'commission(ENter y for yes): '))
else:
    print("thanks for using my program.")