#strings and tuples are same both are immutable data types in python where as lists are mutable data type

tuple=(1,2,3,4,5)
print(tuple)
print(type(tuple))

print(tuple[0]) #to access an element using index
print(tuple[1])

print(len(tuple)) #length of tuple


#tuple object doesnot support item assignment same as strings we can access but not change the value of an element in a tuple using index

tup=()
print(tup) #empty tuple 

tupp=(1,) #tuple with one element we need to add a comma after the element
print(tupp)
#if we dont give a comma it will be considered as an integer and not a tuple
#tuppp=(1) #this is not a tuple this is an integer

#slicing
print(tuple[1:4]) #to access a range of elements from index 1 to 3
print(tuple[:4]) #to access elements from the beginning to index 3


#tuple methods
tuplee=(2,1,3,1)
print(tuplee.index(1)) #to find the index of the first occurrence of an element

print(tuplee.count(1)) #to count the number of occurrences of an element in a tuple