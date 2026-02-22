
try:
    year = int(input("Enter a year: "))

    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(f"{year} is a Leap Year.")
        print("Reason: Divisible by 4 and (not divisible by 100 unless divisible by 400).")
    else:
        print(f"{year} is NOT a Leap Year.")
        print("Reason: Does not satisfy leap year conditions.")

except ValueError:
    print("Invalid input. Enter a valid year.")