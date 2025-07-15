max = 5
total = 0.0

print("this program calculates the sum of")
print(max, 'numbers you will enter')

for counter in range(max):
    number = int(input('Enter anumber: '))
    total = total + number

print(f"the total is {total}")
