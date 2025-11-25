a = 5
b = 10

sum = a + b

# Normal formatting
print("Language is {}".format("python"))
print("sum of {} & {}".format(a, b, sum))

# index based formating

print("sum of {1} & {0}".format(a, b, sum))

# value based formatting 
print("value of vars {a} & {b}".format(a = 5, b = 10))