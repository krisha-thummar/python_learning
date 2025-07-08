expenses=  []

while True:
    print("--expense tracker--")
    print("1. Add expenses")
    print("2. view expenses")
    print("3. View total spent")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        amount = input("Enter amount: ")
        category= input("Enter category: ")
        expenses.append({"expense":amount,"category":category})
        print("Your expenses has been added to the expenses list")

    elif choice == "2":
        if not expenses:
            print("No expenses added yet.")
        else:
            for expense in expenses:
                print(expense["expense"]," ",expense["category"].capitalize())

    elif choice == "3":
        for expense in expenses:
            print("Total: ", sum(expense["expense"]), expense["category"])

    elif choice == "4":
        break

    else:
        print("Invalid choice.")





