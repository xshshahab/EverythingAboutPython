tuple1 = (0, 1, 2, 4, 2, 1, 0, 3, 2, 1, 0, 3)

print("Length of this tuple:", len(tuple1))

print("Count of 3 in tuple1 is:", tuple1.count(3))

print("Index of 3 in tuple1 is:", tuple1.index(3))

# index(element(Value), startIndex, endIndex)
res = tuple1.index(3, 4, 9)
print("Count of 3 in tuple1 is:", res)