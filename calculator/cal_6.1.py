#Clear specific history entry

import math
results = []
history = []

def basic_calc():
    print("Available Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View history")
    print("6. Clear history")
    print("7. Clear specific history entry")
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
    print("10. View history")
    print("0. Exit")


print("Welcome to the OOP Calculators!")
print('')
print("Choose calculator type: ")
print("1. Basic Calculator")
print("2. Scientific Calculator")
print('')

choice = input("Enter choice:")
print('')

if choice == "1":
    print("You have selected: Basic Calculator")
    print('')
    basic_calc()

    while True:
        print('')
        choice = input("Enter your choice(0-7): ")

        if choice == "1":
            print("You have selected Addition")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 + num2
            results.append(total)
            x =  f"Addition: {num1} + {num2} = {total}"
            history.append(x)
            print(f"Result: {num1} + {num2} = {total} ")

        elif choice == "2":
            print("You have selected Subtraction")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 - num2
            results.append(total)
            x = f"Subtraction: {num1} - {num2} = {total}"
            history.append(x)
            print(f"Result: {num1} - {num2} = {total} ")

        elif choice == "3":
            print("You have selected Multiplication")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 * num2
            results.append(total)
            x = f"Multiplication: {num1} * {num2} = {total}"
            history.append(x)
            print(f"Result: {num1} * {num2} = {total} ")

        elif choice == "4":
          try:
             print("You have selected Division")
             num1 = int(input("Enter the first number: "))
             num2 = int(input("Enter the second number: "))
             total = num1 / num2
             results.append(total)
             x = f"Division: {num1} / {num2} = {total}"
             history.append(x)
             print(f"Result: {num1} / {num2} = {total} ")
          except ZeroDivisionError:
             print("Error: Division by zero")
             results.append(0)
             x = f"Division: {num1} / {num2} = Error : Division by zero"
             history.append(x)

        elif choice == "5":
            print("You have selected: View history")
            print("Operation history:")
            if len(history) < 1:
                print("(No operations recorded)")

            for i in range(len(history)):
                print(f"{i+1}. {history[i]}")

        elif choice == "6":
            history.clear()

        elif choice == "7":
            print("You have selected: Clear specific history entry")
            print('')
            length = len(history)
            if length < 1:
                print("No history entries to delete.")
            elif length >= 1:
                print("Current operation history:")
                for i in range(length):
                    print(f"{i+1}. {history[i]}")

                    delete = int(input(f"Enter the number of the entry to delete(1-{length}): "))
                    if delete > length :
                        print(f"Invalid entry number. Please enter a number between 1 and {length}.")
                        delete = int(input(f"Enter the number of the entry to delete 1-{length}): "))
                        print(f"History entry #{delete} {history[delete - 1]} has been deleted.")
                        history.pop(delete - 1)
                    else:
                        print(f"History entry #{delete} {history[delete - 1]} has been deleted.")
                        history.pop(delete - 1)

        elif choice == "0":
            print("Thank you for using the calculator")
            break

        else:
            print("Invalid choice")

elif choice == "2":
    print("You have selected: Scientific Calculator")
    scienific_calc()

    while True:
        choice = input("Enter your choice(0-10): ")

        if choice == "1":
            print("You have selected Addition")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 + num2
            results.append(total)
            x = f"Addition: {num1} + {num2} = {total}"
            history.append(x)
            print(f"Result: {num1} + {num2} = {total} ")

        elif choice == "2":
            print("You have selected Subtraction")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 - num2
            results.append(total)
            x = f"Subtraction: {num1} - {num2} = {total}"
            history.append(x)
            print(f"Result: {num1} - {num2} = {total} ")

        elif choice == "3":
            print("You have selected Multiplication")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 * num2
            results.append(total)
            x = f"Multiplication: {num1} * {num2} = {total}"
            history.append(x)
            print(f"Result: {num1} * {num2} = {total} ")

        elif choice == "4":
            try:
                print("You have selected Division")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                total = num1 / num2
                results.append(total)
                x = f"Division: {num1} / {num2} = {total}"
                history.append(x)
                print(f"Result: {num1} / {num2} = {total} ")
            except ZeroDivisionError:
                print("Error: Division by zero")
                results.append(0)
                x = f"Division: {num1} / {num2} = Error : Division by zero"
                history.append(x)

        elif choice == "5":
            print("You have selected Power")
            num1 = int(input("Enter base number: "))
            num2 = int(input("Enter exponent: "))
            total = num1 ** num2
            results.append(total)
            x = f"Power: {num1} ^ {num2} = {total}"
            history.append(x)
            print(f"Result: {num1} ^ {num2} = {total} ")

        elif choice == "6":
            print("You have selected Modulus")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            total = num1 % num2
            results.append(total)
            x = f"Modulus: {num1} % {num2} = {total}"
            history.append(x)
            print(f"Result: {num1} % {num2} = {total} ")

        elif choice == "7":
            print("You have selected Square root")
            num1 = int(input("Enter number: "))
            total = math.sqrt(num1)
            results.append(total)
            x = f"Sqrt({num1}) = {total}"
            history.append(x)
            print(f"Result: sqrt({num1})  = {total} ")

        elif choice == "8":
            last_result = results[-1]
            print(f"Last result: {last_result} ")

        elif choice == "0":
            print("Thank you for using the calculator")
            break

        elif choice == "9":
            scienific_calc()

        elif choice == "10":
            for i in range(len(history)):
                print(f"{i+1}. {history[i]}")

        else:
            print("Invalid choice")


