# Q15: Prime Number Checker

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

try:
    number = int(input("Enter a number: "))

    if is_prime(number):
        print(f"{number} is a PRIME number")
    else:
        print(f"{number} is NOT a prime number")

    # Range part
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    print("Prime numbers in range:")
    primes = []

    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)

    print(primes)

except ValueError:
    print("Invalid input.")