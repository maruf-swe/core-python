print("""== Equal to

!= Not equal to

< Less than

> Greater than

<= Less than or equal to

>= Greater than or equal to

True and True=True

True and False=False

False and True=False

False and False=False

""")

print("Mixing Boolean and Comparison Operators")
print((4 < 5) and (4 < 5))

print("if Condition")
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

print("else")
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')

print("elif")

age = 10
name = "maruf"
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

print("while loop")

spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

print("break statement")

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

print(" Continue statement ")

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
