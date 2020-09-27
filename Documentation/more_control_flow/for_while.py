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
