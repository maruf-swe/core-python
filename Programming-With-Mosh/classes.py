class Point:
    def move(self):
        print("Draw")

    def draw(self):
        print("Move")


point1 = Point()
point1.move()
point1.x = 10
print(point1.x)

class Talk:
    def __init__(self, x):
        self.x = x

    def talk(self):
        print(f"Hi am {self.x}")

talk = Talk("Marufur Rahman")
talk.talk()

class Human:
    def talk(self):
        print("Human can talk")

class Man(Human):
    def height(self):
        print("His height is 5 ft")

man = Man()
man.talk()
man.height()