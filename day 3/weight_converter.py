weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted:.2f} kilos.")
else:
    converted = weight / 0.45
    print(f"Your weight is {converted:.2f} pounds.")
