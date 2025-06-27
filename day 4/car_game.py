command = ""

while command.lower != "exit":
    command = input(">")
    if command.lower() == "start":
        print("Welcome to Car Game")
        print("The car is started..")
    elif command.lower() == "stop":
        print("The car is stopped..")
    elif command.lower() == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("exit - to quit")
    elif command.lower() == "exit":
        print("Goodbye")
    else:
        print("I don't understand that...")