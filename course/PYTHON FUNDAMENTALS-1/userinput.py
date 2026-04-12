#how to take input from user/terminal
#input is a function which is used to take input from user

username=input("enter your name: ")
print("hello",username)

#sum of two numbers
num1=input("enter first number: ")
num2=input("enter second number: ")
print("sum is",num1+num2)
#the output is not correct because input function takes input as string by default
#a="5" b="10" sum is "510" because it concatenates the two strings instead of adding them as numbers    
#to convert string to int we can use int() function

num1=int(input("enter first number: "))
num2=int(input("enter second number: ")) #type casting- converting one data type to another
print("sum is",num1+num2)


#gets an error if we enter a float number because it cannot convert a float to int directly
#to handle this, we can use float() function instead of int() function
num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
print("sum is",num1+num2)