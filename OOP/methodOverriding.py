class Math:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def sum(self):
        return self.x + self.y


class Mathextended(Math):
    def __init__(self, x, y):
        super().__init__(x, y)

    def subtract(self):
        print(self.x - self.y)

    def sum(self):
        return self.x + self.y + 100

    def show_all(self):
        print(super().sum())
        print(self.sum())


math2 = Mathextended(10, 2)
math2.show_all()
