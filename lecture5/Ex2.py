def generate_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(str(i))

    return ", ".join(primes)

print(generate_primes(10))  
print(generate_primes(20))  
print(generate_primes(1))   
print(generate_primes(2))   
