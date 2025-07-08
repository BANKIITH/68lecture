
print("""Please select operation
      1.Add
      2.Subtract
      3.Multiply
      4.Divide""")

choose = input("select 1,2,3,4: ")

number1 = float(input("enter the first number: "))
number2 = float(input("enter the second number: "))

if choose == "1":
    result = number1 + number2
    print(f"result = {result} ")
elif choose == "2":
    result = number1 - number2
    print(f"result = {result}")   
elif choose == "3":
    result = number1 * number2
    print(f"result = {result}")   
elif choose == "4":
    result = number1 / number2
    print(f"result = {result}")
else:
    print("Wrong. plese select 1,2,3,4")


