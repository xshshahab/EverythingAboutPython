# issuperset_example_with_subset.py

# Defining sets
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4}
set_c = {6, 7}

# Checking if set_a is a superset of set_b (True)
print("set_a is a superset of set_b:", set_a.issuperset(set_b))

# Checking if set_b is a superset of set_a (False)
print("set_b is a superset of set_a:", set_b.issuperset(set_a))

# Checking if set_a is a superset of set_c (False)
print("set_a is a superset of set_c:", set_a.issuperset(set_c))
