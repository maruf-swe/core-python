words = ['banana', 'dragon', 'apple', 'pineaple']
for w in words:
    print(w, len(w))

words = {'b': 'banana', 'd': 'dragon', 'a': 'apple', 'p': 'pineaple'}
for key, w in words.items():
    print(key, w)

# r range function
for i in range(10):
    print(i)

for i in range(5, 20):
    print(i)
for i in range(5, 20, 3):
    print(i)

    # range() and len()

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])

#range function and sum
print(sum(range(4)))

print(range(10))
print(list(range(4)))

# break statement

for i in range(10):
    if i == 2:
        print("Loop is finished when i =", i)
        break
# break statements with else for
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# continue statements

for i in range(6):
    if i == 3:
        continue
    print(i)
# continue statements with else for
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    continue
print("Found an odd number", num)

# pass statement

for i in range(10):
    pass
