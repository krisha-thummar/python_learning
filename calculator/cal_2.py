import math

print("Welcome to the OOP Calculators!")

print("Choose calculator type: ")
print("1. Basic Calculator")
print("2. Scientific Calculator")

choice = input("Enter choice :")
if choice == "1":
    print("You have selected: Basic Calculator")
    print("Available Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    while True:

        choice = input("Enter your choice(0-4): ")

        if choice == "1":
            print("You have selected Addition")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 + num2
            print(f"Result: {num1} + {num2} = {total} ")
        elif choice == "2":
            print("You have selected Substraction")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 - num2
            print(f"Result: {num1} - {num2} = {total} ")
        elif choice == "3":
            print("You have selected Multiplication")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 * num2
            print(f"Result: {num1} * {num2} = {total} ")
        elif choice == "4":
            print("You have selected Division")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 / num2
            print(f"Result: {num1} / {num2} = {total} ")
        elif choice == "0":
            print("Thank you for using the calculator")
            break

elif choice == "2":
    print("You have selected: Scientific Calculator")

    print("Available Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7.Square root")
    print("0. Exit")

    while True:
        choice = input("Enter your choice(0-7): ")

        if choice == "1":
            print("You have selected Addition")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 + num2
            print(f"Result: {num1} + {num2} = {total} ")
        elif choice == "2":
            print("You have selected Substraction")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 - num2
            print(f"Result: {num1} - {num2} = {total} ")
        elif choice == "3":
            print("You have selected Multiplication")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 * num2
            print(f"Result: {num1} * {num2} = {total} ")
        elif choice == "4":
            print("You have selected Division")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 / num2
            print(f"Result: {num1} / {num2} = {total} ")
        elif choice == "5":
            print("You have selected Power")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 ** num2
            print(f"Result: {num1} ** {num2} = {total} ")
        elif choice == "6":
            print("You have selected Modulus")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 % num2
            print(f"Result: {num1} % {num2} = {total} ")
        elif choice == "7":
            print("You have selected Square root")
            num1 = int(input("Enter number: ")
            total = math.sqrt(num1)
            print(f"Result: sqrt({num1})  = {total} ")
        elif choice == "0":
            print("Thank you for using the calculator")
            break


