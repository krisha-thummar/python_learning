x = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
target = 8
found = False

print(len(x))
print(len(x[0]))
for i in range(len(x)):
   for j in range(len(x[i])):
       if x[i][j] == target:
           print(f"found at row{i} and column{j}")
           found = True
           break
   if found:
       break