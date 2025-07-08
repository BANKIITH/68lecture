worked = (int(input("Enter the number of hours worked:")))
hourly_pay = (int(input("Enter the hoursly pay rate:")))


if worked > 40:
    regular = 40 * hourly_pay 
    Overtime = worked - 40
    Overtime_pay = (Overtime * 1.5) * hourly_pay
    gross_pay = regular + Overtime_pay 

else:
    gross_pay = worked * hourly_pay
    
print(f"the gross pay is {gross_pay:.2f}")

