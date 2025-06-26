# AND, OR, NOT

has_good_grades = True
applied_loan = False

if has_good_grades and not applied_loan:
    print("Has good grades!")
    print("You are eligible for scholarship and loaning.")
elif has_good_grades and applied_loan:
    print("That's great. You can continue further process.")