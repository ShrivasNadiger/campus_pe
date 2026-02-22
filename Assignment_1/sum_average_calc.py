# Q13: Sum and Average Calculator

try:
    count = int(input("How many numbers? "))

    numbers = []

    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)

    total = sum(numbers)
    average = total / count if count > 0 else 0

    print("\n=== RESULTS ===")
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

except ValueError:
    print("Invalid input.")