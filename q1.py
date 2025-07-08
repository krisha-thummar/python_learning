n = 0
print("Welcome to the OOP Calculator!")
print("------------------------------")

current_result = 0.0
print("Current result: ", current_result)

while n == 0:
    print("Choose one operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. power")
    print("7. clear result")
    print("8. Exit")

    choice = input("Enter choice(1-8): ")

    if choice == "1":
        x = float(input("enter a number :"))
        current_result += x
        print("Current_result: ", current_result)
    elif choice == "2":
        y = float(input("Enter a number: "))
        current_result -= y
        print("Current_result: ", current_result)
    elif choice == "3":
        y = float(input("Enter a number: "))
        current_result *= y
        print("Current_result: ", current_result)
    elif choice == "4":
        try:
            y = float(input("Enter a number: "))
            current_result /= y
            print("Current_result: ", current_result)
        except ZeroDivisionError:
            print("ERROR : division by zero!")
            print("Current_result: ", current_result)
    elif choice == "5":
        y = float(input("Enter a number: "))
        current_result **= y
        print("Current_result: ", current_result)
    elif choice == "6":
        y = float(input("Enter a number: "))
        current_result //= y
        print("Current_result: ", current_result)
    elif choice == "7":
        current_result = current_result * 0
        print("Result cleared.")
        print("Current_result: ", current_result)
    elif choice == "8":
        print("Exit")
        break


