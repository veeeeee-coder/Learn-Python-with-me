info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# 1.list all unique courses
unique_courses=set()
for tup in info:
    unique_courses.add(tup[1])
print(unique_courses)

for val in info:
    if val[1]=="English":
        print(val[0])

dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
#update() → creates the key with an empty set
#add() → puts the course inside that set
#You need both because:
#Without update() → no container exists
#Without add() → container exists but empty

