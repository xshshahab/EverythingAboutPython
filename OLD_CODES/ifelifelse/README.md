# Python If, Else, and Elif Statements

## What are If, Else, and Elif in Python?

`if`, `else`, aur `elif` Python ke conditional statements hain jo program ke flow ko kisi condition ke basis par control karte hain.

---

## Key Features:

- **`if` Statement**:

  - Ek condition ko test karta hai.
  - Agar condition `True` hoti hai, toh iske neeche wala code execute hota hai.

- **`else` Statement**:

  - Agar `if` ki condition `False` ho, toh ye execute hota hai.

- **`elif` (short for "else if") Statement**:
  - Multiple conditions ko check karne ke liye use hota hai.
  - Agar iska condition `True` ho, toh iske neeche wala code execute hota hai.
  - Ye `if` ke baad aur `else` ke pehle likha jata hai.

---

## Syntax:

```python
if condition:
    # Code to execute if condition is True
elif another_condition:
    # Code to execute if another_condition is True
else:
    # Code to execute if none of the conditions are True
```

### Example Code:

```python
# Example 1: Basic If-Else
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example 2: Using Elif
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Example 3: Nested If-Else
number = 5

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")
```

## How It Works (in Simple Terms):

- Python conditions ko upar se neeche check karta hai.
- Jo bhi pehli `True` condition hoti hai, uska block execute hota hai.
- Agar koi bhi condition `True` nahi hoti:
- else block execute hota hai (agar present ho).
- Indentation ka dhyan rakhna zaroori hai:
- `if`, `elif`, aur `else` ke andar ka code properly indented hona chahiye.
