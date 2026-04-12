#lists and tuples are kinda equivalent to arrays in other languages, but they can hold different types of data

#a built in data type that stores set of values
#it can store elements of different data types

marks=[55,67.6,89,69.99,80,90]
print(marks)
print(type(marks))
#somewhat similar to func of strings

print(marks[0]) #to access an element using index
print(marks[1])

print(len(marks)) #length of list

student=["geetha",98,"Kerala"]
print(student)
print(student[0])

#strings are immuable but lists are mutable
#we can change the value of an element in a list using index

student[1]=95 #changing the value at index 1
print(student)

#in strings we can access but not chnage, but in lists we can access and change the value of an element using index

#slicing
print(marks[1:4]) #to access a range of elements from index 1 to 3
print(marks[:4]) #to access elements from the beginning to index 3
print(marks[2:4]) #to access elements from index 2 to 3
print(marks[3:]) #to access elements from index 3 to the end
print(marks[-1]) #to access the last element
print(marks[-3:-1]) #to access the last 3 elements


#list methods

list=[2,1,3]
list.append(4) #to add an element at the end of the list
print(list)

list.sort() #to sort the list in ascending order
print(list)

list.sort(reverse=True) #to sort the list in descending order
print(list)

list.reverse() #to reverse the order of the list
print(list)

list.insert(1,5) #to insert an element at a specific index
print(list)

listt=["litchi","mango","banana"]
listt.sort() #to sort the list in ascending order
print(listt)


listtt=[2,1,3,1]
listtt.remove(1) #to remove the first occurrence of an element
print(listtt)

listtt.pop(0) #to remove an element at a specific index and return it
print(listtt)