def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)

    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits

    if total == number:
        print("True")
        return True
    else:
        print("False")
        return False


is_armstrong(153)
is_armstrong(9474)
is_armstrong(123)
