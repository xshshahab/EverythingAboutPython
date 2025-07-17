s1 = {"Tokyo", "Korea", "Japan"}
s2 = {"Korea", "Instanbul", "USA"}

s3 = s1.intersection(s2)
print("intersection :", s3)

print(s1, s2)


s1.intersection_update(s2)
print("Intersection Update :", s1)
print(s1)
