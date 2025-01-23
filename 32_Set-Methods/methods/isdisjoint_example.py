# isdisjoint_example.py

# Defining two sets
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
set3 = {4, 5, 6, 7}

# Using isdisjoint() method to check if sets are disjoint
print("set1 and set2 are disjoint:", set1.isdisjoint(set2))  # Expected True
print("set1 and set3 are disjoint:", set1.isdisjoint(set3))  # Expected False
