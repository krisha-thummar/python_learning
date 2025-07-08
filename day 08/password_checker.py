password = input("enter a password: ")

if len(password) < 8:
    print("your passoword is too short")
else:
    print("checkig further conditions...")

has_upper = False
has_lower = False
has_numbers = False
has_special_chars = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_numbers = True
    elif char in '!@#$%^&*=+?/':
        has_special_chars = True

if has_upper and has_lower and has_numbers and has_special_chars:
    print("Strong Password")
elif (has_upper or has_lower) and has_numbers:
    print("Medium Password")
else:
    print("Weak Password")