names = ['Maruf', 'Isha', 'Pranti', 'Iqra']
print(names)
print(names[2])
print(names[-1])
print(names[2:3])
print(names[2:])
print(type(names))


numbers = [3,2,5,6,7,8,1]
sor = sorted(numbers)[-1]
print(sor)

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)