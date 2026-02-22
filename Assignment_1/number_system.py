# Q20: Number System Functions

import math

def factorial(n):
    return math.factorial(n)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

def reverse_number(n):
    return int(str(n)[::-1])

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def is_perfect_number(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def math_menu():
    while True:
        print("\n=== MATH MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == '10':
            break

        try:
            if choice == '1':
                n = int(input("Enter number: "))
                print("Factorial:", factorial(n))

            elif choice == '2':
                n = int(input("Enter number: "))
                print("Prime:", is_prime(n))

            elif choice == '3':
                n = int(input("Enter n: "))
                print("Fibonacci:", fibonacci(n))

            elif choice == '4':
                n = int(input("Enter number: "))
                print("Sum of digits:", sum_of_digits(n))

            elif choice == '5':
                n = int(input("Enter number: "))
                print("Reversed:", reverse_number(n))

            elif choice == '6':
                n = int(input("Enter number: "))
                print("Armstrong:", is_armstrong(n))

            elif choice == '7':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))

            elif choice == '8':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))

            elif choice == '9':
                n = int(input("Enter number: "))
                print("Perfect Number:", is_perfect_number(n))

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input")

math_menu()