try:
    age = int(input("Age: "))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("can't divided by zero")
except ValueError:
    print('Invalid Value')