def find_divisors(n: int) -> list[int]:
    if n <= 0:
        return []
   
    divisors = [i for i in range(1, n + 1) 
                if n % i == 0]
        
    return sorted(divisors)
    
print("Welcome to the Divisor Finder!")
print(find_divisors((int(input(f"Enter a number: ")))))