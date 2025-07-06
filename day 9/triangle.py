# draw l-triangle
row = 5

for i in range(1,row+1):
    for j in range(i):
        print(" * ",end = '')
    print()

# multiplication table
for i in range(1,6):
    number = 5
    print(f"{number} * {i} = {number*i}")
print()

# 5*5 table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j}", end='\t')
    print()

#print elements row by row
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in mat:
    for col in row:
        print(col, end='\t')
    print()