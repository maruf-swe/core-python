string1 = "yes, they said"
print(string1)
string2 = 3 * "un" + "ium"
print(string2)
print('py' + 'thon')
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
print("multiple strings")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
x = 'python'
print('j' + x[1:])

print("strings are array")
print(x[1])
print(len(x))
a = " Hello, World! "  # remove white space
print(a.strip())
a = "Hello, World!"
print(a.lower())

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, I am " + str(age)
print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = f"I want {quantity} pieces of item {itemno} for {price} dollars."
print(myorder)

print("String Format w3 schools")
txt = "50800"
x = txt.isdigit()
print(x)
