'''input in python
is used to accept values from user
for 
string- input()
integer- int(input())
float- float(input())'''

name=input( "enter your name: ") #this will take input from user and return it as a string
print("heyyyy", name)
print(type(name),name)
#here all input is considered as string by default

age=int(input("enter your age: ")) #this will take input from user and convert it to integer
print("your age is", age)

height=float(input("enter your height: ")) #this will take input from user and convert it to float
print("your height is", height)