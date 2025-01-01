# Strings are immutable

name = "sohan"
print(name.upper()) # Output: SOHAN

name2 = "ORHAN"
print(name2.lower()) # Output: orhan

un_name = "Harish !!!"
print(un_name.rstrip("!")) # Output: Harish

print(un_name.replace("Harish", "Rajesh")) # Output: Rajesh !!!

notes = "a day was man died when he is running."
print(notes.capitalize()) # Output: The day a man died when he is running.

welcome_center = "Welcome to programming in python"
print(welcome_center.center(80)) 
#                   Output: Welcome To Programming In Python
