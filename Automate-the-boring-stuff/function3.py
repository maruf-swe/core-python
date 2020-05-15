import random

print("example 1")


def hello(name):
    print('Hello, ' + name)


hello('Alice')
hello('Bob')

print("example 2")


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

print("Example 3")
print("local and global variable with same name")

def spam():
    eggs = 'spam local'
    print(eggs)  # prints 'spam local'


def bacon():
    eggs = 'bacon local'
    print(eggs)  # prints 'bacon local'
    spam()
    print(eggs)  # prints 'bacon local'


eggs = 'global'
bacon()
print(eggs)

print("example 4")
print("function as a black box")

def spam1(divideBy):
    return 42 / divideBy

print(spam1(2))
print(spam1(12))
print(spam1(0))
print(spam1(1))

print("keyword argument")
def great_users(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome")


great_users(last_name="Maruf", first_name="Ahmed")
