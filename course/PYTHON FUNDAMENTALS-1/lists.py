#4 important built in datastructures in python they are
#lists 
#tuples
#dictionaries
#sets

#1.lists are ordered, mutable, and allow duplicate elements. They are defined using square brackets [] and can contain elements of different data types.
#for ex take marks instead of marks for 5 subjects we can use a list to store the marks of the subjects.saves memory and we can easily access the marks of each subject using indexing.
marks=[85,90,78,92,88]
print(marks)
print(len(marks))
print(marks[0]) #accessing the first element of the list
marks[0]=95 #modifying the first element of the list
print(marks)
#which is impossible in strings becz theyre immutable
print(type(marks)) #type of the list 
#can do slicing in lists as well
print(marks[1:4]) #prints the marks from index 1 to 3

#list methods are functions in python lists are classes and methods are functions that are defined inside a class. we can use the methods to perform various operations on the list. some of the commonly used list methods are append(), insert(), remove(), pop(), sort(), reverse(), etc. 
l=[1,2,3]
l.append(67) #adds an element to the end of the list
print(l)
l.insert(1,45) #inserts an element at the specified index
print(l)
l.sort() #sorts the list in ascending order
print(l)

l.sort(reverse=True) #sorts the list in descending order
print(l)

l.reverse() #reverses the order of the list
print(l)


#as list is a sequential data we use for loop to iterate through the list and perform operations on each element of the list. we can also use while loop to iterate through the list using indexing.

fruit=["apple","banana","mango"]
for boo in fruit:
    print(boo)


lisst=[1,2,3,45,6,67]
for val in lisst:
    if val==67:
        print("found")
        break
    else:
        print("not found")


nums=[1,2,3,10,4]
x=10
idx=0
for val in nums:
    if val==x:
        print(f"{x} found at index {idx}")
        break
    idx+=1
#also called linear search algorithm as we are searching for an element in a list by iterating through the list sequentially until we find the element or reach the end of the list.
