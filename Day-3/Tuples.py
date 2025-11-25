# tup = (1, 2, 3, 4, 5, "abc", 3.14)

# print(tup[2])

# print(tup)
# print(len(tup))

# print(tup[0:3])

tup = (1, 2, 3, 4, 5,3.14)
print(tup.count(2))

sum = 0
for val in tup:
    sum += val
    
print(f"sum of vals is {sum}")
