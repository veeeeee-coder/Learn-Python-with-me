#repeat redundant tasks
count=1 #iterator
while count<=6:
    print("vee",count)
    count+=1
print(count)

num=5
while num>=1:
    print(num)
    num-=1


num=int(input("enter num:"))
i=1
while i<=10:
    print(num,"x", i, "=",num*i)
    i+=1

#break statement- used to exit the loop when a certain condition is met
i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1#updation is imp to avoid infinite loop
print("loop ended")

#continue statement- used to skip the current iteration and move to the next iteration of the loop
i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i) #prints only odd numbers from 1 to 9




#for loop- used to iterate over a sequence (like list, tuple, string) or other iterable objects
 
string="veeee"
#in => membership operator- checks if a value is present in a sequence or not
for var in string:
    print(var)


string="geetha"
if "e" in string:
    print("e is present in string")


#for numbers its 0 to n-1
for i in range(5): #0,1,2,3,4 if i+1 is done then it will be 1,2,3,4,5
    print(i)


word="artificial intelligence"
count=0
for char in word:
    if char=="i":
        count+=1
print("count of i is",count)