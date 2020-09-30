"""A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression."""
# lambda arguments : expression

x = lambda a: a + 10
print(x(5))

# lambda can take any number of arguments
x = lambda a, b: a * b
print(x(5, 6))

# Why Use lambda
""" The power of lambda is better shown when you use them as an 
anonymous function inside another function.
Use that function definition to make a function that always doubles the number you send in:"""


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
