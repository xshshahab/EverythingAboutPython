# Iterate over the keys and print each key and its value.

user = {
    "name": "Syphar",
    'age': "21",
    "email": "example@syphar.com",
    "city": "New York",
    "country": "USA",
    "is_married": "false",
}

for key in user.keys():
    print(key)
    print(user[key])
