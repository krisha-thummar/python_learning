# list methods

list1 = ['krisha', 'meet', 'riya','sahil']
print(list1)
list2 = list1.copy()
print(list1[0])
print(list1[1:])
print(list1.append('sahil'))
print(list1.index('sahil'))
print(list1.count('sahil'))
print(list1.pop())
print(list1.remove('sahil'))

print(list2)

# remove duplicates from a list
numbers = [4,1,2,4]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)