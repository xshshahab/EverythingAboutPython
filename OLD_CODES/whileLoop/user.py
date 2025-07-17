# Take input from user until it's give the maximum of our requirements.


i = int(input("Start the number game give me a number, and which number you want to reach: "))

# Keep asking for input until the number entered is greater than 20
while i <= 50:
    print(f"You entered: {i}")
    i = int(input("Enter the number: "))

print("You're Done!!")
