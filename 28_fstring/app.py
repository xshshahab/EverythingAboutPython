name = "Harsh"
country = "India"

# This syntax is also correct
# letter = "Hey, My name is {} and I am from {}".format(name, country)

letter = "Hey, My name is {} and I am from {}"

print(letter.format(name, country))

# using f string method
print(f"Hey, My name is {name} and I am from {country}")