#collection of unique elements
#sets are mutable which means that we can change the values of the sets. we can add or remove elements from the sets. but we cannot change the value of an element in the set because sets are unordered and do not support indexing. we can also use the add() method to add elements to the set and the remove() method to remove elements from the set. if we try to add an element that already exists in the set, it will not be added again because sets do not allow duplicate elements.
#sets are defined using curly braces {} and the elements are separated by commas. we can also use the set() constructor to create a set from a list or a tuple. sets are also called unordered collection of unique elements in other programming languages.

#every element in the set should be immutable which means that we cannot change the value of an element in the set. if we try to change the value of an element in the set, it will raise a TypeError. but we can add or remove elements from the set because sets are mutable.
#s = {(1, 2)}          # ✅ allowed
#s = {(1, [2, 3])}     # ❌ NOT allowed (list inside tuple)
#Immutable objects can be added to a set
#Mutable objects cannot be added to a set

#In Python, a set can only contain immutable (unchangeable) elements because it relies on hashing, which requires values to stay constant after being added; therefore, types like numbers (int, float), strings, and tuples (only if all their elements are also immutable) can be added to a set, while mutable types like lists and dictionaries cannot be added since they can change their contents, which would break how the set tracks and stores them internally.

set={1,2,3,3,2,2,2,2,1,4,5,5,5}
print(set) #prints the set with unique elements only
print(type(set))
#only a single value of 5 is added to the set because sets do not allow duplicate elements
print(len(set)) #prints the number of unique elements in the set
#they are unordered collection of unique elements so we cannot access the elements of the set using indexing. we can use a for loop to iterate through the elements of the set.

set.add(6) #adds an element to the set
print(set)
#empty set
#empty_set=set() #creates an empty set using the set() constructor not like empty_set={} because it creates an empty dictionary not a set
#print(empty_set)

set.remove(2) #removes an element from the set
print(set)

#set.clear() #removes all the elements from the set
#print(set) #prints an empty set

set.pop() #removes an random element from the set and returns it. since sets are unordered, we cannot predict which element will be removed. if the set is empty, it will raise a KeyError.
print(set)

set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) #returns a new set that contains all the elements from both sets
print(set1.intersection(set2)) #returns a new set that contains only the elements that are present in both sets
print(set1.difference(set2)) #returns a new set that contains only the elements that are present in the first set but not in the second set
print(set1.symmetric_difference(set2)) #returns a new set that contains only the elements that are present in either of the sets but not in both sets
