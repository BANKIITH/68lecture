mother_number = int(input("Enter number to Multiply: "))

print("Number\Square")
print("-------------")

for num in range(1,13):
    square = num*mother_number
    print(f"{num} * {num}=\t{square}")