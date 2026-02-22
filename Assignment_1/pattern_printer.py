# Q11: Number Pattern Printer

try:
    print("\nChoose Pattern:")
    print("1. Increasing Numbers")
    print("2. Repeating Row Numbers")
    print("3. Reverse Decreasing")
    print("4. Pyramid Pattern")

    choice = int(input("Enter pattern number: "))
    height = int(input("Enter height: "))

    print("\n")

    if choice == 1:
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif choice == 2:
        for i in range(1, height + 1):
            print((str(i) + " ") * i)

    elif choice == 3:
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    elif choice == 4:
        for i in range(1, height + 1):
            # Left increasing
            for j in range(1, i + 1):
                print(j, end="")
            # Right decreasing
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    else:
        print("Invalid pattern choice.")

except ValueError:
    print("Invalid input. Please enter numbers only.")