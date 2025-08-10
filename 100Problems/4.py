def calculate_sum_and_average() -> None:
    numbers = []
    

    for i in range(1, 6):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)
    

    total = sum(numbers)
    average = total / len(numbers)
    

    print(f"Sum: {total:.2f}")
    print(f"Average: {average:.2f}")

print("Welcome to the Sum and Average Calculator!")
calculate_sum_and_average()
print("Thank you for using the calculator!")