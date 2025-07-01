weight, height = float(input("Enter your weight: ")) , float(input("Enter your hight in meters: "))

bmi = weight / (height * height)
print('your BMI is: ', format(bmi, '1,.2f'))