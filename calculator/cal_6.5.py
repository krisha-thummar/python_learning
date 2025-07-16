# User context and Sessions

import math
import random

class BasicCalculator:
    def __init__(self):
        self.history = []
        self.results = []
        self.last_operation = {}
        self.user = ''
        self.greet = ["ready for some calculations?",
                      "Don't be a square, let's solve some math!",
                      "Need a little math magic? I'm here to help!",
                      "Let's make math fun again! What can I calculate for you?",
                      "Feeling numeric? I'm your huckleberry.",
                      "Ready to calculate? Let's go!",
                      "I'm your friendly calculator."]

    def username(self,username):
        self.user = username
        print(f"Hello, {self.user}! {random.choice(self.greet)}")

    def basic_calc(self):
        print("\nAvailable Operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View history")
        print("6. Clear history")
        print("0. Exit")

    def sum(self,num1,num2):
        total = num1 + num2
        self.results.append(total)
        x = f"Addition: {num1} + {num2} = {total}"
        self.history.append(x)
        self.last_operation.update({'type':'add', 'value':num2 , 'name':'Addition','symbol':'+'})
        return f"Result: {num1} + {num2} = {total} "

    def sub(self,num3,num4):
        total = num3 - num4
        self.results.append(total)
        x = f"Subtraction: {num3} - {num4} = {total}"
        self.history.append(x)
        self.last_operation.update({'type': 'Subtract', 'value': num4, 'name': 'Subtraction', 'symbol': '-'})
        return f"Result: {num3} - {num4} = {total} "

    def mul(self,num5,num6):
        total = num5 * num6
        self.results.append(total)
        x = f"Multiplication: {num5} * {num6} = {total}"
        self.history.append(x)
        self.last_operation.update({'type': 'Multiply', 'value': num6, 'name': 'Multiplication', 'symbol': '*'})
        return f"Result: {num5} * {num6} = {total} "

    def div(self,num7,num8):
        try:
            total = num7 / num8
            self.results.append(total)
            x = f"Division: {num7} / {num8} = {total}"
            self.history.append(x)
            self.last_operation.update({'type': 'Divide', 'value': num8, 'name': 'Division', 'symbol': '/'})
            return f"Result: {num7} / {num8} = {total} "
        except ZeroDivisionError:
            self.results.append(0)
            x = f"Division: {num7} / {num8} = Error : Division by zero"
            self.history.append(x)
            self.last_operation.update({'type': 'Divide', 'value': num8, 'name': 'Division by zero', 'symbol': '/'})
            return "Error: Division by zero"

    def view_history(self):
        print(f"{self.user}'s Operation history:")
        if len(self.history) < 1:
            print("No operations recorded")
        else:
            for i in range(len(self.history)):
                print(f"{i + 1}. [{self.user}] {self.history[i]}")
        return None

    def clear_history(self):
        return self.history.clear()

    def clear_entry(self):
        print("You have selected: Clear specific history entry")
        print('')
        length = len(self.history)
        if length < 1:
            return "No history entries to delete."
        elif length >= 1:
            print("Current operation history:")
            for i in range(length):
                print(f"{i + 1}. {self.history[i]}")

                delete = int(input(f"Enter the number of the entry to delete(1-{length}): "))
                if delete > length:
                    print(f"Invalid entry number. Please enter a number between 1 and {length}.")
                    delete = int(input(f"Enter the number of the entry to delete 1-{length}): "))
                    print(f"History entry #{delete} {self.history[delete - 1]} has been deleted.")
                    self.history.pop(delete - 1)
                else:
                    print(f"History entry #{delete} {self.history[delete - 1]} has been deleted.")
                    self.history.pop(delete - 1)

    def last_result(self):
        print("You have selected last result")
        if self.results:
            last_result = self.results[-1]
            return f"Last result: {last_result} "
        else:
            return "No results available yet."

    def switch_calc(self,to_calc):
            to_calc.history = self.history.copy()
            to_calc.results = self.results.copy()
            print("Transferring your data...")
            if self.results:
                print(f"- Last result: {self.results[-1]}")
            else:
                print("- No previous result available.")
            print(f"- History: {len(self.history)} operations transfered.")
            print("- Variables: 0 variables transferred")

    def repeat_operation(self):
        if len(self.history) < 1:
                print("\nError: No previous operation to repeat.")
                print("Please perform an operation first, then you can repeat it.")
        else:
            print(f"Last operation: {self.last_operation['type']} ({self.last_operation['symbol']} {self.last_operation['value']})")

            if self.last_operation['value'] == 0 and self.last_operation['symbol'] == '/':
                print("Repitition failed.")
                print("Error: Divsion by zero")

            else:
                repetitions = input("Enter number of repetitions:")
                print(f"\nRepeating '{self.last_operation['name']} {self.last_operation['symbol']} {self.last_operation['value']}' {repetitions} times...")

                last_result = self.results[-1]
                for i in range(int(repetitions)):
                    value = self.last_operation['value']
                    operand = self.last_operation['symbol']
                    if operand == '+':
                        print(f"Repetition {i + 1}: {last_result} + {value} = {last_result + value}")
                        self.history.append(f"Addition: {last_result} + {value} = {last_result + value}")
                        last_result = last_result + value
                    elif operand == '-':
                        print(f"Repetition {i + 1}: {last_result} - {value} = {last_result - value}")
                        self.history.append(f"Subtraction: {last_result} - {value} = {last_result - value}")
                        last_result = last_result - value
                    elif operand == '*':
                        print(f"Repetition {i + 1}: {last_result} * {value} = {last_result * value}")
                        self.history.append(f"Multiplicatiion: {last_result} * {value} = {last_result * value}")
                        last_result = last_result * value
                    elif operand == '/':
                        print(f"Repetition {i + 1}: {last_result} / {value} = {last_result / value}")
                        self.history.append(f"Division: {last_result} / {value} = {last_result / value}")
                        last_result = last_result / value

                print("\nAll repetitions complete!")
                print(f"Final result : {last_result}")

    def compare_numbers(self,u,v):
        if float(u) > float(v):
            x = f"Comparison: {u} is greater than {v}."
            self.history.append(x)
            print(f"Result: {u} is greater than {v}.")
        elif float(u) < float(v):
            x = f"Comparison: {u} is less than {v}."
            self.history.append(x)
            print(f"Result: {u} is less than {v}.")
        elif float(u) == float(v):
            x = f"Comparison: {u} is equal to {v}."
            self.history.append(x)
            print(f"Result: {u} is equal to {v}.")

class ScientificCalculator(BasicCalculator):

    def scientific_calc(self):
        print("\nAvailable Operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square root")
        print("7. View history")
        print("8. Clear history")
        print("0. Exit")

    def power(self,base,exponent):
        total = base ** exponent
        self.results.append(total)
        x = f"Power: {base} ^ {exponent} = {total}"
        self.history.append(x)
        return f"Result: {base} ^ {exponent} = {total} "

    def modulus(self,a,b):
        total = a % b
        self.results.append(total)
        x = f"Modulus: {a} % {b} = {total}"
        self.history.append(x)
        return f"Result: {a} % {b} = {total} "

    def sqrt(self,y):
        total = math.sqrt(y)
        self.results.append(total)
        x = f"Sqrt({y}) = {total}"
        self.history.append(x)
        return f"Result: sqrt({y})  = {total} "

    def sine(self,k):
        total = math.sin(k)
        self.results.append(total)
        x = f"Sine({k}) = {total}"
        self.history.append(x)
        return f"Result: {k} sine({k}) = {total} "

    def cosine(self,j):
        total = math.cos(j)
        self.results.append(total)
        x = f"Cosine({j}) = {total}"
        self.history.append(x)
        return f"Result: {j} Cosine{j} = {total} "

    def logarithm(self,i):
        total = math.log(i)
        self.results.append(total)
        x = f"Logarithm({i}) = {total}"
        self.history.append(x)
        return f"Result: {i} Logarithm({i}) = {total} "

class CalculatorApp:

    def __init__(self):
        self.basic = BasicCalculator()
        self.scientific = ScientificCalculator()
        self.greetings = ["Have a great day !", "See you next time!", "Keep up the great calculations!"]

    def run(self):

        print("Welcome to the OOP Calculators!")
        username = input("Enter your username: ").strip()
        while not username or len(username) < 1:
            print("Username cannot be empty. Please enter a valid username.")
            username = input("Enter your username: ").strip()
        self.basic.username(username)

        while True:
            print('')
            print("Choose calculator type: ")
            print("1. Basic Calculator")
            print("2. Scientific Calculator")
            print('')
            choice = input("enter choice: ")
            if choice == "1":
                self.run_basic_mode()
            elif choice == "2":
                self.run_scientific_mode()
            else:
                print("Invalid choice.Try again.")


    def run_basic_mode(self):
        print("You have selected: Basic calculator")
        self.basic.basic_calc()

        while True:
            choice = input("\nEnter your choice(0-8): ")

            if choice == "1":
                print("You have selected Addition")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(self.basic.sum(num1, num2))

            elif choice == "2":
                print("You have selected Subtraction")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(self.basic.sub(num1, num2))

            elif choice == "3":
                print("You have selected Multiplication")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(self.basic.mul(num1, num2))

            elif choice == "4":
                print("You have selected Division")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(self.basic.div(num1, num2))

            elif choice == "5":
                print("You have selected View History")
                self.basic.view_history()

            elif choice == "6":
                print("You have selected Clear History")
                self.basic.clear_history()

            elif choice == "0":
                print("You have selected: Exit")
                print(f"Thank you for using the calculator, {self.basic.user}. Goodbye!")
                print(random.choice(self.greetings))
                break

            else:
                print("Invalid input. Please try again.")


    def run_scientific_mode(self):

        self.scientific.user = self.basic.user
        print("You have selected: Scientific Calculator")
        self.scientific.scientific_calc()

        while True:
            choice = input("\nEnter your choice(0-13): ")

            if choice == "1":
                print("You have selected Addition")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(self.scientific.sum(num1, num2))

            elif choice == "2":
                print("You have selected Subtraction")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(self.scientific.sub(num1, num2))

            elif choice == "3":
                print("You have selected Multiplication")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(self.scientific.mul(num1, num2))

            elif choice == "4":
                print("You have selected Division")
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(self.scientific.div(num1, num2))

            elif choice == "5":
                print("You have selected Power")
                num1 = float(input("Enter the base number: "))
                num2 = float(input("Enter the exponent: "))
                print(self.scientific.power(num1, num2))

            elif choice == "6":
                print("You have selected Square root")
                num1 = float(input("Enter number: "))
                print(self.scientific.sqrt(num1))

            elif choice == "7":
                print("You have selected View history")
                self.scientific.view_history()

            elif choice == "8":
                print("You have selected clear history")
                self.scientific.clear_history()

            elif choice == "0":
                print("You have selected: Exit")
                print(f"Thank you for using the calculator, {self.scientific.user}. Goodbye!")
                print(random.choice(self.greetings))
                break

            else:
                print("Invalid choice. Please try again.")


calculator = CalculatorApp()
calculator.run()






