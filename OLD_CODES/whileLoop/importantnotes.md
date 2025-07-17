- Python doesn't have a built-in `do-while` loop, but you can emulate it using a `while` loop. The key characteristic of a `do-while` loop is that it guarantees the loop body will run at least once, and then continues looping as long as a condition remains true.

**`do-while` behavior:**

1. Execute the loop body at least once.
2. After the loop body, check the condition to decide if it should repeat.

### How to emulate a `do-while` loop in Python:

You can use a `while` loop with an initial condition set to `True` to ensure the loop runs at least once. After executing the loop body, you can check the condition at the end of the loop.

### Example: Emulating a `do-while` loop

```python
# Emulate do-while using a while loop in Python

while True:
    # Loop body - this will run at least once
    number = int(input("Enter a number (enter 0 to stop): "))

    if number == 0:
        break  # Exit the loop if the condition is met

    print(f"You entered: {number}")

print("You're done!")
```

## How this works:

1. The while True makes sure that the loop continues indefinitely (like the do-while loop).
2. Inside the loop, the user is prompted to enter a number.
3. If the user enters 0, the loop is exited using break.
4. The loop body runs at least once because the condition is checked after the body is executed.

##### Output example:

```python
Enter a number (enter 0 to stop): 5
You entered: 5
Enter a number (enter 0 to stop): 10
You entered: 10
Enter a number (enter 0 to stop): 0
You're done!
```
