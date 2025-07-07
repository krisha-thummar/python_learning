print("Welcome to the OOP Calculator!")
print("------------------------------")

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





