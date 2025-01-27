employee1 = {
    122 : 54,
    433 : 87,
    194 : 89,
    234 : 54
}

employee2 = {
    812 : 54,
    654 : 87,
}

print("Senior Manager",employee1)
print("Junior Manager", employee2)

employee1.update(employee2)
print(employee1)

# employee1.clear()
# print(employee1)

# employee1.pop(122)
# print(employee1)

# employee2.popitem()
# print(employee2)

# del employee2
# del employee2[654]
# print(employee2)