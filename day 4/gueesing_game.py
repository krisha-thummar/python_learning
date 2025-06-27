print("You have 3 chances to guess the number.")

secret_number = 2

guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess the number:"))
    guess_count += 1
    if guess == secret_number:
        print("you won!")
        break

else:
    print("Sorry, you lose :|")
