class Car:
    def __init__(self, name, color, speed):
        self.name = name  #public_variable
        self.__color = color #private_variable
        self.__speed = speed 

    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.__color = color

    def set_speed(self, speed):
        self.__speed = speed

    def get_name(self):
        return self.name

    def get_color(self):
        return self.__color

    def get_speed(self):
        return self.__speed


car1 = Car('Bmw', 'Blue', 500)
car2 = Car('Ford', 'Black', 450)
car3 = Car('Walton', 'White', 400)

print(car1.get_name())
print(car1.get_color())
print(car1.get_speed())

car1.set_name("Suzuki")
print(car1.get_name())
car2.name = "Hyundi"
print(car2.name)
print(car2.color)