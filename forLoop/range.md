# range() in python

In Python, the built-in range() function generates a sequence of numbers. It is commonly used in loops, such as for loops. The range() function can take one, two, or three parameters:

## 1. **Single Parameter (range(stop))**

When `range()` is called with a single parameter, it is interpreted as the stop value. The sequence starts at 0 and increments by 1 up to, but not including, the stop value.

```python
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

## 2. **Two Parameters (range(start, stop))**

When called with two parameters, the first parameter is the start value, and the second is the stop value. The sequence starts at start and increments by 1 up to, but not including, the stop value.

```python

for i in range(2, 6):
print(i)

# Output:
# 2
# 3
# 4
# 5
```

## 3. **Three Parameters (range(start, stop, step))**

When called with three parameters, the first is the start value, the second is the stop value, and the third is the step, which determines the increment (or decrement, if negative) between numbers in the sequence.

```python

for i in range(1, 10, 2):
print(i)

# Output:
# 1
# 3
# 5
# 7
# 9
```
