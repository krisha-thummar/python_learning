# Exit Confirmation

class Calculator:
    def __init__(self):
        self.history = []
        self.last_operation = {}

    def menu(self):
        print("\n=== Calculator Menu ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View history")
        print("6. Save history")
        print("0. Exit")

    def sum(self,num1,num2):
        total = num1 + num2
        print(f"Result: {num1} + {num2} = {total}")
        self.history.append(f'Addition: {num1} + {num2} = {total}')

    def sub(self,num3,num4):
        total = num3 - num4
        print(f"Result: {num3} - {num4} = {total}")
        self.history.append(f'subtraction: {num3} - {num4} = {total}')

    def mul(self,num5,num6):
        total = num5 * num6
        print(f"Result: {num5} * {num6} = {total}")
        self.history.append(f'Multiplication: {num5} * {num6} = {total}')

    def div(self,num7,num8):
        try:
            total = num7 / num8
            print(f"Result: {num7} / {num8} = {total}")
            self.history.append(f'Division: {num7} / {num8} = {total}')
        except ZeroDivisionError:
            x = f"Division: {num7} / {num8} = Error : Division by zero"
            print(x)
            self.history.append(f"Error(Division by zero): {num7} / {num8} = {total}")

    def view_history(self):
        print(f"Current Operation history:")
        if len(self.history) < 1:
            print("No operations recorded")
        else:
            for i in range(len(self.history)):
                print(f"{i + 1}. {self.history[i]}")

    def save_history(self):
        print("History saved to file: calculator_history.txt")
        with open("calculator_history.txt", "w") as file:
            file.writelines(self.history)
        self.last_operation.update({'status': "Saved"})


class CalculatorApp:

        def __init__(self):
            self.basic = Calculator()

        def run(self):
            while True:
                self.basic.menu()
                choice = input("\nChoose operation: ")

                if choice == '5':
                    self.basic.view_history()

                elif choice == '6':
                    self.basic.save_history()

                elif choice == '0':
                    print("Are you sure you want to exit?")
                    x = input("(y/n): ").lower()

                    if x == "y":
                        if self.basic.history and self.basic.last_operation.get('status') != "Saved":
                            print(f"You have {len(self.basic.history)} operations in history that haven't been saved.")
                            confirm = input("Are you sure you want to exist (y/n): ").lower()
                            if confirm == "y":
                                print("Thank you for using calculator! Goodbye!")
                                break
                            else:
                                print("Returning to main menu...")
                                continue
                        else:
                            print("Thank you for using calculator! Goodbye!")
                            break

                    elif x == "n":
                        print("Returning to main menu...")
                        continue
                    else:
                        print("Invalid input. Returning to main menu...")
                        continue

                elif choice in ['1', '2', '3', '4']:
                    try:
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                    except ValueError:
                        print("Invalid input! Please enter numeric values.")
                        continue

                    if choice == '1':
                        self.basic.sum(num1, num2)
                    elif choice == '2':
                        self.basic.sub(num1, num2)
                    elif choice == '3':
                        self.basic.mul(num1, num2)
                    elif choice == '4':
                        self.basic.div(num1, num2)
                else:
                    print("Invalid choice. Please select a valid option from the menu.")


calc = CalculatorApp()
calc.run()