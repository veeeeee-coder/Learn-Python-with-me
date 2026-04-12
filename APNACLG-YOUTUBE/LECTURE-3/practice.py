#wap to take 3 movie names from user and store them in a list and print the list and its type
names1=input("enter movie name1: ")
names2=input("enter movie name2: ")
names3=input("enter movie name3: ")
list=[names1,names2,names3]
print(list)
print(type(list))


#movies=[]
# mov1=input("enter movie name1: ")
# mov2=input("enter movie name2: ")   
# mov3=input("enter movie name3: ")
# movies.append(mov1)



#palindrome using copy and reverse method
list1=[1,2,3,2,1]
revv=list1[::-1] #to reverse the list using slicing
if list1==revv:
    print("palindrome") 
else:  
    print("not palindrome")


list2=[1,"abc","abc",1]
revv=list2.copy() #to create a copy of the list
revv.reverse() #to reverse the order of the list    
if list2==revv:
    print("palindrome")
else:
    print("not palindrome")




#count no of times "A" OCCURED in tuple
grade=("B","A","C","A","B","A","C","B","A")
print(grade.count("A")) #to count the number of occurrences of an element in a list


#store above values in list and sort the list in ascending order
gradee=["B","A","C","A","B","A","C","B","A"]
gradee.sort() #to sort the list in ascending order
print(gradee)