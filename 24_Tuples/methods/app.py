# Defining a tuple of countries
countries = ("Spain", "Finland", "Italy", "India", "England")
print(countries)  # Print the initial tuple

# Convert the tuple to a list
temp = list(countries)
print("Temp :", temp)  # Print the list form of the tuple

# Append "Russia" to the list
temp.append("Russia")
print("Temp after append:", temp)  # Print the list after appending

# Remove the element at index 3 ("India") using pop
temp.pop(3)
print("Temp after pop:", temp)  # Print the list after removing an element

# Change the value at index 2 from "Italy" to "Turkie"
temp[2] = "Turkie"
print("Temp after index assignment:", temp)  # Print the list after updating an element

# Convert the list back to a tuple
countries = tuple(temp)
print(countries)  # Print the updated tuple
