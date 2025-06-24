try:
    num = int(input("enter the number: "))
    ber = int(input("Enter the secound number: "))

    result = num + ber

    print(f"the awnser is: {result}")
except ValueError:
    print("please type numbers only")