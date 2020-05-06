teamparature = 40

if teamparature > 35:
    print("Its hot Day")
else:
    print("It's not hot Day")

if teamparature >= 35:
    print("Its hot Day")
else:
    print("It's not hot Day")

if teamparature <= 35:
    print("Its hot Day")
else:
    print("It's not hot Day")

if teamparature != 35:
    print("Its hot Day")
else:
    print("It's not hot Day")

if teamparature == 35:
    print("Its hot Day")
else:
    print("It's not hot Day")


name = input("Please insert your name: ")
if len(name) < 3:
    print("Name must be 3 character")
elif len(name) > 50:
    print("Name can be Maximum 50 character")
else:
    print("Name look good")