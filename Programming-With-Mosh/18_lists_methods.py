numbers = ['a', 'i', 'o', 'u', 2, 3, 4, 2]
numbers.sort()
numbers.append('m')
numbers.reverse()
numbers.clear()
counting = numbers.count('i')
print(counting)

uniques = []
for i in numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)
