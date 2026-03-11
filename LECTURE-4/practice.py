dicct={
    "table":["a piece of furniture",
             "list of facts and figures"
             ],
    "cat":"a small animal"
}
print(dicct)


subjects={
    "python","cpp","java","python","javascript","cpp","java","python","cpp","java","rust"}

print(len(subjects)) #to get the number of unique elements in the set

marks={}
x=int(input("enter physics marks: "))
marks.update({"physics":x}) #to add a key:value pair to the dictionary using update() method
y=int(input("enter chemistry marks: ")) 
marks.update({"chemistry":y})
z=int(input("enter maths marks: "))
marks.update({"maths":z})
print(marks)

yelloww={9,9.0}
print(yelloww) #in sets 9 and 9.0 are considered as the same element because they are equal in value and have the same hash value
red={9,"9.0"}
print(red) #in sets 9 and "9.0" are considered as different elements because they are of different data types and have different hash values

vvalue={
    ("float",9.0),
    ("int",9)
}
print(vvalue) #in sets ("float",9.0) and ("int",9) are considered as different elements because they are of different data types and have different hash values