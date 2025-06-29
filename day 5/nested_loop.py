# print this using nested loop
"""
        xxxxx
        xx
        xxxxx
        xx
        xx
"""

set1 = [5,2,5,2,2]

for i in set1:
    output = ''
    for count in range(i):
        output += 'x'
    print(output)

