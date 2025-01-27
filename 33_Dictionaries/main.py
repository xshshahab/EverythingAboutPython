user = {
    "name" : "Syphar",
    'age' : "21",
    "email" : "example@syphar.com",
    "city" : "New York",
    "country" : "USA",
    "is_married" : "false",
}

print(user)
print("Username :",user["name"])
print("Username :",user.get("name"))

print(user.keys())
print(user.values())

print(user.items())

for key in user.keys():
    print(key)
    print(user[key])


for key in user.keys():
    print(f" The key corresponding key is {key} and it's value is {user[key]}")


for key,value in user.items():
    print(f" The key corresponding key is {key} and it's value is {value}")