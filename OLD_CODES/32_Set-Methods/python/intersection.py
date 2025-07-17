s1 = {1, 2, 4, 3, 5, 6}
s2 = {7, 8, 3, 4, 5, 6}

s3 = s1.intersection(s2)
print("Intersection :", s3)

print(s1, s2)


s1.intersection_update(s2)
print("Update :", s1)
print(s1)
