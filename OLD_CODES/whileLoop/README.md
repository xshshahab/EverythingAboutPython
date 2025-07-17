# While loop.

In Python, a `while` loop is used to execute a block of code repeatedly as long as a given condition is `True`. Here's the general syntax:

```python
while condition:
    # Code to execute
```

## **Key Points:**

**1. Condition:** The loop checks the condition at the beginning of each iteration. If the condition is `True`, the loop body executes. If the condition is `False`, the loop terminates.

**2. Infinite Loop:** If the condition never becomes `False`, the loop will run forever. To avoid this, ensure the condition eventually evaluates to `False`.

### Example 1: Counting with a `while` loop

```python
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
```

###### Output:

```python
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

### Example 2: Using `break` to Exit a `while` Loop

```python
count = 0
while True:  # Infinite loop
    count += 1
    print("Count is:", count)
    if count == 5:
        break  # Exit the loop
```

###### Output:

```python
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

### Example 3: Using `continue` to Skip Iteration

```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop for this iteration
    print("Count is:", count)
```

###### Output:

```python
Count is: 1
Count is: 2
Count is: 4
Count is: 5
```

### Example 4: Using `else` with a `while` Loop

```python
count = 0
while count < 3:
    print("Count is:", count)
    count += 1
else:
    print("Finished looping!")
```

###### Output:

```python
Count is: 0
Count is: 1
Count is: 2
Finished looping!
```

- The `else` block executes when the loop condition becomes `False` naturally (i.e., without a `break` statement).
