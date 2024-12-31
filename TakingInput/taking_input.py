name = input("Enter you name : ")
print("Your name is : ", name)

age = input("Enter you age : ")
print("Your age is : ",age, type(age)) # give string type because input always return string
# This is also a way to conver string into number 
# print("Your age is : ", int(age)) # this will give error because int() function

# another method 

my_age = int(input("Enter your current age : "))
print("Your age is : ", my_age, type(my_age)) # this will give int type 
