name = input("enter your name: ")
age = int(input("enter your age: "))
income = float(input("enter your income: "))

print(f"""here is the data youentered: 
      name: {name}
      age: {age}
      income: {income}  
      """)
print('income: ', format(income, '12,.2f'))