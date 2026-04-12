#dictionary is word meaning pairs
#dictionaries are used to store data values in key:value pairs
#they are unordered,mutable(changeable) and dont allow duplicate keys,not indexed

#"key":value

dict={
    "name":"geetha",
    "age":25,
    "city":"kerala",
    "marks":[66,56,78],
    "is_student":True,
     12.99:96.6
}

print(dict)
print(type(dict))

print(dict["name"]) #to access a value using key
print(dict["age"])  
print(dict["marks"])
print(dict[12.99]) #to access a value using key 


dict["age"]=26 #to change the value of a key
print(dict)

null_dict={} #empty dictionary
print(null_dict)





#nested dictionary

student={
    "name":"geetha",
    "age":25,
    "city":"kerala",
    "marks":[66,56,78],
    "is_student":True,
     12.99:96.6,
     "subjects":{
         "maths":90,
         "science":85,
         "english":88
     }
}
print(student)
print(student["subjects"]) #to access the nested dictionary
print(student["subjects"]["maths"]) #to access a value from the nested dictionary using key



#dictionary methods
dict2={
    "name":"geetha",
    "age":25,
    "city":"kerala",
    "marks":[66,56,78],
    "is_student":True,
     12.99:96.6
}

print(len(dict2)) #to get the number of key:value pairs in the dictionary

print(dict2.keys()) #to get all the keys of the dictionary
print(dict2.values()) #to get all the values of the dictionary
print(dict2.items()) #to get all the key:value pairs of the dictionary as a list of tuples
print(dict2.get("name")) #to get the value of a key using get() method
print(dict2.update({"age":26})) #to update the value of a key using update() method
print(dict2)

print(list(dict2.keys())) #to convert the keys of the dictionary to a list
print(list(dict2.values())) #to convert the values of the dictionary to a lis

student.update({"city":"kochi"}) #to update the value of a key in the nested dictionary
print(student)

