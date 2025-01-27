# For Loop with else in Python

In Python, a `for` loop can be followed by an `else` block. The `else` block will execute if the loop completes without encountering a `break` statement. If the loop is terminated with a `break`, the else block will not execute.

Here’s how the `for` loop with else `works`:

### Syntax:

```python
for item in iterable:
    # loop body
    if condition:
        break
else:
    # else block
    # This will only execute if the loop doesn't get interrupted by a 'break'
```

### Example 1: Without `break`

If the loop runs normally and finishes iterating over the entire iterable, the `else` block will execute.

```python
for i in range(3):
    print(i)
else:
    print("Loop completed without break.")
```

### Output:

```plaintext
0
1
2
Loop completed without break.
```

---

## Example 2: With `break`

If the loop encounters a `break` statement before completing all iterations, the `else` block will not execute.

```python
for i in range(3):
    print(i)
    if i == 1:
        print("Breaking the loop.")
        break
else:
    print("Loop completed without break.")
```

## Output:

```arduino
0
1
Breaking the loop.
```

In this case, since the loop was broken when `i == 1`, the `else` block did not run.

### When to Use `else` in a `for` Loop

The `else` block is typically used when you need to check if a loop completed normally (i.e., without hitting a `break`). It’s common in situations like searching or looking for an item in a collection.

### Example 3: Searching for an item

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        print("Found 3!")
        break
else:
    print("3 not found.")
```

### Output:

```
Found 3!
```

In this case, the `else` block is skipped because the loop was broken when `num == 3`.
