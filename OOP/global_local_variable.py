class Resturent:
    # global variable
    name = 'doi ghor'
    owner = 'Maruf'

    def details(self):
        print(self.name, self.owner)

    def details_with_address(self, address):
        #local variable
        name = 'Rahim'
        print(self.name, self.owner)
        print(address)


restaurant1 = Resturent()
restaurant1.details()
restaurant1.details_with_address("Babor road")
print(type(restaurant1))
