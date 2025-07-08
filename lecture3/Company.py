employees = int(input("Enter the number of employees: "))

if employees < 50:
    print("this is a small company.")
elif employees < 250:
    print("this is a medium company.")
elif employees >= 250:
    print("this is a large company.")