# Iterate over the keys and print a formatted string for each key and its value.

user = {
    "name": "Syphar",
    'age': "21",
    "email": "example@syphar.com",
    "city": "New York",
    "country": "USA",
    "is_married": "false",
}

for key in user.keys():
    print(f"The key corresponding key is {key} and its value is {user[key]}")
