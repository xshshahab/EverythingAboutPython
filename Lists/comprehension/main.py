lst = [i for i in range(1,10)]

print("First List of numbers from 1 to 9: ", lst)

lst2 = [i*i for i in lst]

print("Second list with squares of numbers: ", lst2)

lst3 = [i*i for i in lst if i%2 == 0]

print("Third list with squares of even numbers: ", lst3)