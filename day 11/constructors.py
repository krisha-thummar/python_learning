class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y
        

point1 = Point(10,20)
total = point1.sum()
print(total)




