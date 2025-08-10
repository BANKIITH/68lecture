def find_divisors(n: int) -> list[int]:
    if n <= 0:
        return []
    
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    return sorted(divisors)
print("Welcome to the Divisor Finder!")
print(find_divisors(20))