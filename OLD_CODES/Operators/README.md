# Python Operators

In Python, **operators** are symbols or keywords used to perform operations on values or variables. These operations can include arithmetic calculations, comparisons, logical decisions, and more. Below is a categorized explanation:

---

## **1. Arithmetic Operators**

Used for basic mathematical operations.

- `+` → Addition (`5 + 3 = 8`)
- `-` → Subtraction (`5 - 3 = 2`)
- `*` → Multiplication (`5 * 3 = 15`)
- `/` → Division (`5 / 2 = 2.5`)
- `//` → Floor Division (removes decimals: `5 // 2 = 2`)
- `%` → Modulus (remainder: `5 % 2 = 1`)
- `**` → Exponentiation (power: `5 ** 3 = 125`)

---

## **2. Comparison (Relational) Operators**

Used to compare two values. They return `True` or `False`.

- `==` → Equal to (`5 == 5 → True`)
- `!=` → Not equal to (`5 != 3 → True`)
- `>` → Greater than (`5 > 3 → True`)
- `<` → Less than (`5 < 3 → False`)
- `>=` → Greater than or equal to (`5 >= 5 → True`)
- `<=` → Less than or equal to (`5 <= 3 → False`)

---

## **3. Logical Operators**

Used for combining conditional statements.

- `and` → Both conditions must be `True` (`True and False → False`)
- `or` → At least one condition must be `True` (`True or False → True`)
- `not` → Negates the condition (`not True → False`)

---

## **4. Assignment Operators**

Used to assign values to variables.

- `=` → Assign (`x = 5`)
- `+=` → Add and assign (`x += 3` is the same as `x = x + 3`)
- `-=` → Subtract and assign (`x -= 2` is the same as `x = x - 2`)
- `*=` → Multiply and assign (`x *= 4`)
- `/=` → Divide and assign (`x /= 2`)
- `//=` → Floor divide and assign
- `%=` → Modulus and assign
- `**=` → Exponent and assign

---

## **5. Bitwise Operators**

Work with binary numbers.

- `&` → AND
- `|` → OR
- `^` → XOR
- `~` → NOT
- `<<` → Left shift
- `>>` → Right shift

---

## **6. Membership Operators**

Test for membership in a sequence (like a list, string, etc.).

- `in` → Returns `True` if a value is found in the sequence.
  - Example: `'a' in 'apple' → True`
- `not in` → Returns `True` if a value is not in the sequence.
  - Example: `'z' not in 'apple' → True`

---

## **7. Identity Operators**

Compare memory locations of two objects.

- `is` → Returns `True` if both variables point to the same object.
  - Example: `x is y`
- `is not` → Returns `True` if variables point to different objects.
  - Example: `x is not y`

---

## **8. Special Operators**

- **Ternary Operator**: A one-line conditional.
  - Example: `x = 5 if a > b else 10`
- **Operator Overloading**: Using operators on custom objects.
  - Example: You can define what `+` does for your own classes.

---

## **Tips for Understanding Operators**

1. **Operator Precedence**: Some operators are evaluated before others (`*` before `+`), so use parentheses to clarify.
2. **Shortcuts**: Assignment operators like `+=` save time.
3. **Logical Chaining**: Use logical operators to write cleaner conditions.
   """
