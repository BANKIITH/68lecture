def calulator():
    rows = int(input("how many row: "))
    columns = int(input("how many columns: "))

    for i in range(rows):
        print('*' * columns)

print("welcome to calculator")
calulator()
