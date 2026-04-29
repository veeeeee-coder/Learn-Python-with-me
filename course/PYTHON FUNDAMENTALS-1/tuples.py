#tuples are immutable, ordered, and allow duplicate elements. They are defined using parentheses () and can contain elements of different data types.
#tuples are similar to lists but they are immutable, which means that once a tuple is created, it cannot be modified. This makes tuples more efficient than lists in terms of memory and performance. Tuples are often used to store related data that should not be changed, such as the coordinates of a point in a 2D space or the RGB values of a color.

tup=(8,9,"uia",True,8) #tuple with different data types and duplicate elements
print(tup)
print(len(tup)) #length of the tuple
print(tup[0]) #accessing the first element of the tuple
print(tup[-1]) #accessing the last element of the tuple
#cant do tup[0]=10 because tuples are immutable like strings

tupp=(1) #expression
print(type(tupp)) #type of the variable tupp is int because it is not a tuple, it is just an integer. to create a tuple with a single element, we need to add a comma after the element.
tupp=(1,) #tuple with a single element
print(type(tupp)) #type of the variable tupp is now tuple because it is a tuple with a single element.
#slicing and indexing works the same way in tuples as in lists and strings because they are all ordered data types. we can use for loop to iterate through the elements of the tuple as well.
print(tup[1:4]) #slicing the tuple from index 1 to 3
tuppie=[9,7,6]
sum=0
for val in tuppie:
    sum+=val
print(f"Sum: {sum}")


#methods in tuples are functions that are defined inside the tuple class. we can use the methods to perform various operations on the tuple. some of the commonly used tuple methods are count(), index(), etc.
print(tup.count(8)) #counting the occurrences of 8 in the tuple 
print(tup.index(8)) #finding the index of the first occurrence of 8 in the tuple