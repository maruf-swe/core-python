coordinates = (1, 2, 3, 4)
x, y, z, m = coordinates
print(m)

coordinate = (1,"Maruf", "Esha", "Pranti", 3, 4)
x, *y, z = coordinate
print(y)
coordinat = (1,"Maruf", "Esha", "Pranti", 3, 4)
x, y, *z = coordinat
print(*z)

numbers = [1, 2, 3, 4, 5]
x, y, z, m, n = numbers
print(x, y, z, m)
