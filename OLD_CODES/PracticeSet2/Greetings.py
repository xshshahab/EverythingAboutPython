import time

# Get the current time
timeStamp = time.strftime('%H:%M:%S')
hourTime = int(time.strftime("%H"))  # Convert hour to integer

print("Current hour:", hourTime)
print("Current timestamp:", timeStamp)

# Determine the greeting based on the hour
if (hourTime >= 0 and hourTime < 12):
    print("Good morning, sir!")
elif (hourTime >= 12 and hourTime < 18):
    print("Good afternoon, sir!")
else:
    print("Good evening, sir!")
