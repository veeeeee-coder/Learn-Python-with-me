#dictionary is key value pair
#dictionary is mutable which means that we can change the values of the keys in the dictionary.
#dictionary is unordered which means that the order of the keys in the dictionary is not guaranteed. we can access the values of the keys in the dictionary using the keys. we can also use the get() method to access the values of the keys in the dictionary. if the key is not present in the dictionary, it will return None instead of raising an error.
#dictionary is defined using curly braces {} and the key value pairs are separated by commas. the key and value are separated by a colon :.
#dictionary is also called associative array or hash map in other programming languages.

#key always should be unique in the dictionary. if we try to add a key that already exists in the dictionary, it will overwrite the existing value of that key.


info={
    "name":"John",
    "age":30,
    "city":"New York",
    "subjects":["Math","Science","English"],
    3.14:"PI"

}
print(info)
print(type(info))

print(info["name"]) #accessing the value of the key "name"
print(info["age"]) #accessing the value of the key "age"
print(info[3.14]) #accessing the value of the key 3.14

#mutable and unordered
info["name"]="Jane" #changing the value of the key "name"
print(info["name"]) #accessing the value of the key "name" after changing it

#methods of dictionary
dictkeyss=info.keys() #returns a view object that contains the keys of the dictionary
print(dictkeyss)
#can be converted to a list
dictkeyss_list=list(dictkeyss)  
print(dictkeyss_list)
print(type(dictkeyss_list))

dictvals=info.values() #returns a view object that contains the values of the dictionary
print(dictvals)

#key value pairs
dictitems=info.items() #returns a view object that contains the key value pairs of the dictionary
print(dictitems)

#gets value according to the key
print(info.get("name")) #returns the value of the key "name"

#we have two ways to access a value of a key in the dictionary. one is using the square brackets [] and the other is using the get() method. the difference between them is that if we try to access a key that is not present in the dictionary using square brackets [], it will raise a KeyError. but if we try to access a key that is not present in the dictionary using the get() method, it will return None instead of raising an error. can maintain flow of the program

#if a key is not present in the dictionary, it will return None instead of raising an error. this is useful when we are not sure if a key is present in the dictionary or not. we can use the get() method to access the value of a key without worrying about whether the key is present in the dictionary or not.

print(info.get("country")) #returns None because the key "country" is not present in the dictionary

#print(info["country"]) #raises KeyError because the key "country" is not present in the dictionary

#add new item in the dictionary
info.update({"dessert":"Ice Cream"}) #adds a new key value pair to the dictionary
print(info)
