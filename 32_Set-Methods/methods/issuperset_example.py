# issuperset_example.py

# Defining two sets
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}

# Using issuperset() to check if set1 is a superset of set2
print("set1 is a superset of set2:", set1.issuperset(set2))  # Expected True

# Defining another set
set3 = {6, 7, 8}

# Checking if set1 is a superset of set3
print("set1 is a superset of set3:", set1.issuperset(set3))  # Expected False
