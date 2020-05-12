customer = {
    "name" : "Marufur Rahman",
    "age" : "22",
    "is_verified" : True
}
customer["age"] = 23
print(customer["name"])
print(customer["age"])
print(customer.get("birthdate"))
print(customer.get("birthdate", "1998"))