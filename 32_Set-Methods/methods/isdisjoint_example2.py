# isdisjoint_example2.py

# Defining three different sets
set_a = {"apple", "banana", "cherry"}
set_b = {"dog", "elephant", "fish"}
set_c = {"cherry", "dog", "grape"}

# Using isdisjoint() method to check if sets are disjoint
print("set_a and set_b are disjoint:", set_a.isdisjoint(set_b))  # Expected True
print("set_a and set_c are disjoint:", set_a.isdisjoint(set_c))  # Expected False
print("set_b and set_c are disjoint:", set_b.isdisjoint(set_c))  # Expected False
