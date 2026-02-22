# Bill Splitter for N numner of people 
try:
    #get Input values from the user
    total_bill = float(input("Enter total bill: "))
    people = int(input("Number of people: "))
    tax_percent = float(input("Tax percentage: "))
    tip_percent = float(input("Tip percentage: "))

    #calculate the per person amount after adding tax and tip amount
    tax_amount = total_bill * tax_percent / 100
    after_tax = total_bill + tax_amount
    tip_amount = total_bill * tip_percent / 100
    final_total = after_tax + tip_amount
    per_person = final_total / people


    # print the Bill results 
    print("\n=== BILL BREAKDOWN ===")
    print(f"Subtotal: ₹{total_bill:.2f}")
    print(f"Tax: ₹{tax_amount:.2f}")
    print(f"After tax: ₹{after_tax:.2f}")
    print(f"Tip: ₹{tip_amount:.2f}")
    print(f"Total: ₹{final_total:.2f}")
    print(f"Per person: ₹{per_person:.2f}")

except:
    print("Invalid input.")