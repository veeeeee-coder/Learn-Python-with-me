
#sets is the collection of the unordered items
#each element in set must be unique and immutable but the set itself is mutable means we can add or remove elements from the set but we cannot change the value of an element in the set
#sets are defined using curly braces {} or using the set() constructor


nums={1,2,3,4,5,"vee"}
set2={1,2,2,2}
print(nums)
print(set2) #duplicate values will be removed in sets
print(type(nums))
print(len(set2)) #length of set

collection=set() #empty set
print(type(collection))

collection.add(1) #to add an element to the set
collection.add(2)
collection.add(3)
collection.add("veee")
collection.add((6,7,8))
collection.add([1,2,34,5]) #we cannot add a list to a set because lists are mutable
#error: unhashable type: 'list'(type error)

print(collection)

collection.remove(2) #to remove an element from the set
print(collection)


#collection.clear() #to remove all the elements from the set


print(collection.pop()) #to remove and return an arbitrary element from the set


set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) #to get the union of two sets
print(set1.intersection(set2)) #to get the intersection of two sets