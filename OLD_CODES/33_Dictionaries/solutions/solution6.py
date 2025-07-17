# Iterate over the dictionary using items() and print a formatted string for each key-value pair.

user = {
    "name": "Syphar",
    'age': "21",
    "email": "example@syphar.com",
    "city": "New York",
    "country": "USA",
    "is_married": "false",
}

for key, value in user.items():
    print(f"The key corresponding key is {key} and its value is {value}")
