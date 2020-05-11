for i in range(2):
    for j in range(3):
        print(f"({i}, {j})")


numbers = [5,2,5,2,2]
for numbers_count in numbers:
    output = ''
    for count in range(numbers_count):
        output +='X'
    print(output)
    