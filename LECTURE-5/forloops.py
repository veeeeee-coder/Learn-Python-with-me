#FOR loops
#for loops are used to iterate over a sequence (like a list, tuple, string) or other iterable objects

list=[1,2,3,4,5]
for i in list:
    print(i)


veggies=["potata","tomata","onion","carrot"]
for j in veggies:
    print(j)


tup=(1,2,3,4,5)
for  num in tup:
    print(num)


str="avaaaaa"
for chr in str:
    print(chr)


#whenever u want to traverse data struvtures like list, tuple, string, set, dictionary, use for loops butwhen u want to repeat a block of code a certain number of times, use while loops


#optional else
tr="avaaaaa"
for chr in str:
    print(chr)
else:
    print("iteration is over")


listtt=[1,2,3,4,5,6]
for i in listtt:
    print(i)


listtt=[1,2,3,4,5,6]
x=3
for i in listtt:
    if x==3:
        print("found",x)
        break
    else:
        print("finding...")



#range functions returns a sequence of numbers starting from 0 by default and increments by 1(by default) and stops before a specified number

for el in range(5):
    print(el) #prints 0 to 4

for el in range(1,6):
    print(el) #prints 1 to 5    

for el in range(1,10,2):
    print(el) #prints 1,3,5,7,9 (increments by 2)

#range(start,stop,step) where start is the starting number, stop is the number before which the sequence of numbers will end and step is the increment value (optional)

for i in range(1,10):
    if i%2==0:
        print(i) #prints even numbers from 1 to 9

#for i in range(2,100,2) 


for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)


n=int(input("enter a number"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)  
    



#pass statement is used when u want to write a loop but dont want to execute any code in the loop body, it is a null statement that does nothing when executed

for i in range(1,11):
    pass #to avoid syntax error when u have an empty loop body