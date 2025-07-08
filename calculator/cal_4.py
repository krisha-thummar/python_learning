#show all Operations

import math
results = []

def basic_calc():
    print("Available Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Get last result")
    print("6. Show all operations")
    print("0. Exit")


def scienific_calc():
    print("Available Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Square root")
    print("8. Get last result")
    print("9. Show all operations")
    print("0. Exit")


print("Welcome to the OOP Calculators!")

print("Choose calculator type: ")
print("1. Basic Calculator")
print("2. Scientific Calculator")

choice = input("Enter choice:")
if choice == "1":
    print("You have selected: Basic Calculator")
    basic_calc()

    while True:
        choice = input("Enter your choice(0-6): ")

        if choice == "1":
            print("You have selected Addition")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 + num2
            results.append(total)
            print(f"Result: {num1} + {num2} = {total} ")

        elif choice == "2":
            print("You have selected Substraction")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 - num2
            results.append(total)
            print(f"Result: {num1} - {num2} = {total} ")

        elif choice == "3":
            print("You have selected Multiplication")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 * num2
            results.append(total)
            print(f"Result: {num1} * {num2} = {total} ")

        elif choice == "4":
          try:
             print("You have selected Division")
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             total = num1 / num2
             results.append(total)
             print(f"Result: {num1} / {num2} = {total} ")
          except ZeroDivisionError:
             print("Error: Division by zero")
             results.append(0)

        elif choice == "0":
            print("Thank you for using the calculator")
            break

        elif choice == "5":
            last_result = results[-1]
            print(f"Last result: {last_result} ")

        elif choice == "6":
            basic_calc()

        else:
            print("Invalid choice")

elif choice == "2":
    print("You have selected: Scientific Calculator")
    scienific_calc()

    while True:

        choice = input("Enter your choice(0-9): ")

        if choice == "1":
            print("You have selected Addition")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 + num2
            results.append(total)
            print(f"Result: {num1} + {num2} = {total} ")

        elif choice == "2":
            print("You have selected Substraction")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 - num2
            results.append(total)
            print(f"Result: {num1} - {num2} = {total} ")

        elif choice == "3":
            print("You have selected Multiplication")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 * num2
            results.append(total)
            print(f"Result: {num1} * {num2} = {total} ")

        elif choice == "4":
          try:
             print("You have selected Division")
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             total = num1 / num2
             results.append(total)
             print(f"Result: {num1} / {num2} = {total} ")
          except ZeroDivisionError:
             print("Error: Division by zero")
             results.append(0)

        elif choice == "5":
            print("You have selected Power")
            num1 = int(input("Enter base number: "))
            num2 = int(input("Enter exponent: "))
            total = num1 ** num2
            results.append(total)
            print(f"Result: {num1} ^ {num2} = {total} ")

        elif choice == "6":
            print("You have selected Modulus")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 % num2
            results.append(total)
            print(f"Result: {num1} % {num2} = {total} ")

        elif choice == "7":
            print("You have selected Square root")
            num1 = int(input("Enter number: "))
            total = math.sqrt(num1)
            results.append(total)
            print(f"Result: sqrt({num1})  = {total} ")

        elif choice == "8":
            last_result = results[-1]
            print(f"Last result: {last_result} ")

        elif choice == "0":
            print("Thank you for using the calculator")
            break

        elif choice == "9":
            scienific_calc()

        else:
            print("Invalid choice")


