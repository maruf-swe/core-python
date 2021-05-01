class Math:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def sum(self):
        print(self.x + self.y)


class Mathextended(Math):
    def __init__(self, x, y):
        super().__init__(x, y)

    def subtract(self):
        print(self.x - self.y)


math1 = Math(2, 4)
math1.sum()
math2 = Mathextended(10, 2)
math2.subtract()
