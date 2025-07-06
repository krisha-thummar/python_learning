# comparison operators > < >= <= == !=

name = input("enter your username: ")

if len(name) < 3:
    print("name must be at least 3 characters long")
elif len(name) > 50:
    print("name cannot exceed 50 characters")
else:
    print("name looks good!")