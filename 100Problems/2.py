
def find_multiples_of_three_and_four (start: int, end: int) -> list:

    if start > end:
        return []
    
    multiples = [num for num in range(start, end + 1) if num % 12 == 0]
    return multiples

print(find_multiples_of_three_and_four(10, 50))