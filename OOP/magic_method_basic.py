class Human:
    def __init__(self, id, name, addresses=[], maps={}):
        self.id = id
        self.name = name
        self.addresses = addresses
        self.maps = maps

    # delete attribute method
    def __delattr__(self, item):
        print('Deleting attribute ' + item)
        return object.__delattr__(self, item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__.get(self, item)

    # check this is equal or not
    def __eq__(self, other):
        return self.id == other.id

    # grater than or equal
    def __ge__(self, other):
        print("calling grater than method")
        return self.id >= other.id

    # hash is performed when you when we attempt to set an item in a dictionary/set.
    def __hash__(self):
        return self.id

    def __str__(self):
        return f'id={self.id}. name={self.name}'


human = Human(1, 'Farhad', ['Address1', 'Address1'], {'London': 2, 'UK': 3})
print(human)

human.name = 'maruf'
print(human.name)
del human.addresses

# dict method
# This method returns a dictionary that represents the object.
human = Human(2, 'Malik').__dict__

# __eq__ method
human1 = Human(2, 'Malik')
human2 = Human(2, 'Malik')
print(human1 == human2)

# __ge__
human1 = Human(3, 'Malik')
human2 = Human(1, 'Malika')
print(human1 >= human2)

# calling hash
first = Human(1, 'Farhad')
second = Human(2, 'Malik')
my_set = set([first, second])
print(len(my_set))

"""__sizeof__
This method is called when we execute sys.getsizeof """
