class Math:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def sum(self):
        print(self.x + self.y)


class MathExtended(Math):
    def __init__(self, x, y):
        super().__init__(x, y)

    def subtract(self):
        return self.x - self.y


class MathExtra:
    def division(self, x, y):
        return x / y


class MathExtended2(MathExtended, MathExtra):
    def __init__(self, x, y):
        super().__init__(x, y)

    def multiplications(self):
        return self.x, self.y


math1 = Math(2, 4)
math1.sum()
math2 = MathExtended(10, 2)
math2.subtract()
multiple_inheritence = MathExtended2(10, 2)
print(multiple_inheritence.division(x=multiple_inheritence.x, y=multiple_inheritence.y))
print(multiple_inheritence.division(4,2))
print(multiple_inheritence.subtract())
