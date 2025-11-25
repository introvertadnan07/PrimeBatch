info = [
    ("Alic", "Math"),
    ("Bob", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]


# for tup in info:
#     print(tup)
#     print(tup[0]) # Name
#     print(tup[1]) # Subject

# unique_course = set()

# for tup in info:
#     unique_course.add(tup[1]) # course
    
# print(unique_course)

dict = {}

for name,course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)