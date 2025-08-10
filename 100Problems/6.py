def check_prime(n: int) -> str:
    if n <= 1:
        return "Not prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not prime"

        return "Prime"
    
n = int(input("Enter a number: "))
print(check_prime(n))