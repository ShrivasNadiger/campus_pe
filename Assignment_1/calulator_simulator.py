def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def calculator():
    while True:
        print("\n=== FUNCTION CALCULATOR ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '7':
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(a, b))
            elif choice == '2':
                print("Result:", subtract(a, b))
            elif choice == '3':
                print("Result:", multiply(a, b))
            elif choice == '4':
                print("Result:", divide(a, b))
            elif choice == '5':
                print("Result:", modulus(a, b))
            elif choice == '6':
                print("Result:", power(a, b))
            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input")

calculator()