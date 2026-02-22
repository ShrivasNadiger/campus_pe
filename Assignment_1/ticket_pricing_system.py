
try:
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").strip().lower()
    tickets = int(input("Number of tickets: "))

    # Base price based on age
    if age < 3:
        base_price = 0
        category = "Free"
    elif 3 <= age <= 12:
        base_price = 150
        category = "Child"
    elif 13 <= age <= 59:
        base_price = 300
        category = "Adult"
    else:
        base_price = 200
        category = "Senior"

    total_base = base_price * tickets

    # Weekend discount
    if day in ["friday", "saturday", "sunday"]:
        discount = total_base * 0.20
    else:
        discount = 0

    final_price = total_base - discount

    print("\n=== TICKET BILL ===")
    print("Category:", category)
    print("Base price:", total_base)
    print("Discount:", discount)
    print("Final amount:", final_price)

except ValueError:
    print("Invalid input.")