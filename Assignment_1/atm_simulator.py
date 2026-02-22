# Q10: ATM Simulator

balance = 10000

while True:
    print("\n=== ATM SIMULATOR ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        print("Current Balance: ₹", balance)

    elif choice == '2':
        try:
            deposit_amount = float(input("Enter amount to deposit: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print("Deposit successful!")
                print("New Balance: ₹", balance)
            else:
                print("Enter valid deposit amount.")
        except:
            print("Invalid input.")

    elif choice == '3':
        try:
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount <= 0:
                print("Invalid withdrawal amount.")
            elif withdraw_amount > balance:
                print("Insufficient balance.")
            elif balance - withdraw_amount < 500:
                print("Minimum balance of ₹500 must remain.")
            else:
                balance -= withdraw_amount
                print("Withdrawal successful!")
                print("New Balance: ₹", balance)
        except:
            print("Invalid input.")

    elif choice == '4':
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice. Try again.")