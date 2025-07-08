def greet_user():
    print("Hello user")
    print("How are you?")

print("start")
greet_user()
print("Finish")

#parameters

def sum(num1, num2):
    print(num1 + num2)

#positional argument
print(sum(1, 2))

#keyword argument
print(sum(num2=4,num1=5))

#return statement

def multiplication(n1,n2):
    return n1*n2

n1 = int(input("enter number 1: "))
n2 = int(input("enter number 2: "))
print(multiplication(n1,n2))



