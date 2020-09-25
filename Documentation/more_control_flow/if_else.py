
a = 33
b = 200

if b > a:
    print("b is greater than a")

number = int(input("Please insert the value "))
if number < 0:
    print("Value less than zero")
elif number == 0:
    print("Value Equal zero")
elif number == 1:
    print("Value Equal single")
else:
    print("Value is more")

# short hand if else
a = 500
b = 300
if a > b: print("a is capital")

a = 200
b = 300
print("Print a") if a > b else print("Print B")

# multiple else condition in single line
a = 350
b = 330
c = 450
print("A i greater than b") if a > b else print("=") if a == b else print("B is greater")
# logical condition and
if a > b and b > c:
    print("A is greater")

if a > b or b > c:
    print("A is greater")

# nested if
a = 6
b = 5
if a > b:
    if b > 10:
        print("B is greter than 10")
    else:
        print("B is less than 10")
else:
    print("A is less than B")
