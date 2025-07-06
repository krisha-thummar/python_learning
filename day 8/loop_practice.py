#Q1. Countdown Timer
'''Ask the user for a number and count
    down to 0 with a delay of 1 second between numbers.

✅ Hint: Use time.sleep(1) after import time.
import time

num = int(input("Enter a number: "))
print("countdown started!")
for i in range(num,-1,-1):
    print(i)
    time.sleep(1)

print("Time over !!")'''

#Q2. Sum of N Natural Numbers
#Ask the user to enter a number n. Use a for loop to calculate the sum of numbers from 1 to n.

'''n = int(input("Enter a number: "))
total = 0
for i in range(1,n+1):
    total += i
print(total)'''

'''✅ Q3. Password Try Limit
Allow the user to try entering the password up to 3 times. 
If correct, print "Access granted", otherwise "Access denied" 
after 3 failed attempts.
✅ Password is "Krisha@123" 

attempt = 3
for i in range(attempt):
    password = input("Enter password: ")
    if password == "Krisha@123":
        print("Access granted")
    else:
        print("oops!, incorrect password")
        print("Access denied")
'''

'''✅ Q4. Find All Even Numbers Between 1 and 50
Print all even numbers between 1 and 50 using a for loop and continue.
for i in range(1,50):
    if i % 2 == 0:
        print(i)
'''

'''✅ Q5. Nested Loop: Number Pattern
Print the following pattern using nested loops:

1
1 2
1 2 3
1 2 3 4'''


for i in range(1,5):
    print(" ")
    for num in range(i):
        num += 1
        print(num, end=' ')
