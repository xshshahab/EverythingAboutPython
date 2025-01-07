i = 1

while i < 10:
    if i % 2 == 0:
        print("skip even number")
        i += 1  # Increment 'i' before continuing
        continue  # Skip the even numbers
    print(i)
    i += 1  # Increment 'i' after printing odd numbers
