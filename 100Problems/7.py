def prime_numbers_in_range(start: int, end: int) -> tuple:
    if start < 1 or end < start:
        return ([], 0)
    
    sieve = [True] * (end + 1)
    sieve[0:2] = [False, False]  # 0 และ 1 ไม่ใช่จำนวนเฉพาะ
    
    # สร้าง sieve
    for i in range(2, int(end ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, end + 1, i):
                sieve[j] = False
    
    # สร้าง list ของจำนวนเฉพาะในช่วง
    primes = [num for num in range(start, end + 1) if sieve[num]]
    primes_sum = sum(primes)
    
    return (primes, primes_sum)

# ทดสอบการทำงาน
print(prime_numbers_in_range(10, 20))  # ([11, 13, 17, 19], 60)
