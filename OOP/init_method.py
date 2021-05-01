class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name, self.age, sep='|')


p1 = Person('Maruf', 23)
p1.details()
p1.name = 'Rahman'
p1.details()