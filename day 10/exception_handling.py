try:
    age = int(input("age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid input")
    print("You did not enter a number")
except ZeroDivisionError:
    print("Age cannot be zero")
