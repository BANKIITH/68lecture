def find_non_multiples(start: int, end: int) -> list:
    if start > end:
        return []
    
    non_miutiples = [num for num in range(start, end +1) if num %3 != 0 and num %4 != 0 and num %5 != 0]
    return non_miutiples

print(find_non_multiples(10, 25))