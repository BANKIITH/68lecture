def sum_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total
num = int(input("Enter a number: "))
print("ผลรวมของหลักตัวเลขใน", num, "คือ", sum_digits(num))