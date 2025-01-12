country = ("INDIA", "USA", "GERMANY", "UAE", "TURKEY")

if "TURKEY" in country:
    print("Yes , Turkey is in the list.")
else :
    print("No, Turkey is not in the list.")

tup = country[:]
print(type(tup), tup)

tup2 = tup[1:4]
print(type(tup2), tup2)