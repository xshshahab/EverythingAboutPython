# Example 3: Student Grades
# Imagine you're storing the grades of students in a class. Each student's name is the key, and their grade is the value.

# Dictionary of student grades
grades = {
    "John": "A",
    "Emily": "B",
    "Sam": "A",
    "Anna": "C"
}

# Accessing values
print(grades["Emily"])  # Output: B

# Adding a new student and grade
grades["Mike"] = "B"
print(grades)  # Output: {'John': 'A', 'Emily': 'B', 'Sam': 'A', 'Anna': 'C', 'Mike': 'B'}

# Updating a grade
grades["Anna"] = "B"
print(grades["Anna"])  # Output: B


# Explanation:

# Keys: "John", "Emily", "Sam", "Anna", and "Mike".
# Values: Grades ("A", "B", "C", etc.).
# You can access, add, and update values in a dictionary.