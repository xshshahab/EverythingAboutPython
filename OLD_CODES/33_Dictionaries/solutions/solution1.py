# Print the user dictionary and username using two different methods.

user = {
    "name": "Syphar",
    'age': "21",
    "email": "example@syphar.com",
    "city": "New York",
    "country": "USA",
    "is_married": "false",
}

print(user)
print("Username :", user["name"])
print("Username :", user.get("name"))
