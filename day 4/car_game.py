command = ""
started =False
while True:
    command = input(">").lower()
    if command == "start":
        print("Welcome to Car Game")
        if started:
            print("Car is already started!")
        else:
            started = True
            print("The car is started..")

    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("The car is stopped..")
    elif command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("exit - to quit")
    elif command == "exit":
        print("Goodbye")
        break
    else:
        print("I don't understand that...")
