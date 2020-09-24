print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


def myFunction():
    return True


print(myFunction())


def she_said(is_rain, has_ambrella):
    return is_rain and not has_ambrella


print(she_said(True, True))


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x, int))

x = 200
print(isinstance(x, str))
