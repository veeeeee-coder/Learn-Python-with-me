print("Hi veee!")
'''print is a function name,it completes a work it shows output on screen. input->code(python)->output'''
print("vee","is passionate abt art")
#printing in same line

print(69)
print(35+25)


#Variable is a name given to memory location which stores data. It is used to store and manipulate data in a program.
'''
var=value
name="veee"
age=19
price=23.99
'''

name="veeee" #string
age=20
price=23.99
print("mera naam hai", name) #anything u put in double quotes it prints ditto same whats in there
print("mera age hai", age)
print("mera price hai", price)

'''in variables right side value is assigned to left side variable name. we can change the value of variable by reassigning it.
a=b is not same as b=a. in a=b value of b is assigned to a but in b=a value of a is assigned to b.'''

age2=age
print("age2 is", age2)

'''Identifiers are the names given to variables, functions, classes, etc. in Python. They must follow certain rules:
1. They can only contain letters (a-z, A-Z), digits (0-9), and underscores (_).
2. They cannot start with a digit.
3. They cannot be a reserved keyword in Python (like if, else, for, while, etc.).
4. They are case-sensitive (age and Age are different identifiers).
5. They should be descriptive and meaningful to improve code readability.
Examples of valid identifiers:
name, age, price, my_variable, _private_var
Examples of invalid identifiers: 1name, age!, price@    
'''

print(type(name))
print(type(age))
print(type(price))
old=False
print(type(old))
a=None
print(type(a))
'''data types in python
integers=+ve,-ve,0
Float=decimal numbers
String="vee",'vee',"""vee"""
Boolean=True,False
None= a=None
'''

'''Keywords are reserved words in Python that have a specific meaning and cannot be used as identifiers (variable names, function names, etc.). They are used to define the syntax and structure of the Python language. Some examples of keywords in Python include:
if, else, elif, for, while, break, continue, def, return, class ''' 

#python is case sensitive language, it means that uppercase and lowercase letters are treated as different characters. For example, the variable name "age" is different from "Age". So, it's important to be consistent with the case when naming variables and using keywords in Python.


a1=2
b1=3
sum=a1+b1
diff=a1-b1
product=a1*b1
print("the sum of a1 and b1 is", sum)
print("the difference of a1 and b1 is", diff)
print("the product of a1 and b1 is", product)



#Comments in python are used to explain the code and make it more readable. They are ignored by the interpreter and do not affect the execution of the program. In Python, there are two types of comments:
# Single-line comments: These comments start with a hash symbol (#) and continue until the end of the line. They are used to add brief explanations or notes about the code.
# Example:
# This is a single-line comment
print("Hello, World!")  # This is an inline comment 

# Multi-line comments: These comments are enclosed within triple quotes (''' or """) and can span multiple lines. They are used to provide more detailed explanations or to comment out blocks of code.
# Example: 
''' This is a multi-line comment
This is the second line of the multi-line comment
This is the third line of the multi-line comment
''' 
# (or use control plus forward slash for multi-line comment)

'''Types of operators
1. Arithmetic operators: +, -, *, /, %, //, **
2. Comparison operators: ==, !=, >, <, >=, <= 
3. Logical operators: and, or, not
4. Assignment operators: =, +=, -=, *=, /=, %=, //=, **=
5. Bitwise operators: &, |, ^, ~, <<, >>   
6. Membership operators: in, not in
7. Identity operators: is, is not'''

#division result is float
#arithmatic operators
a=5
b=2
print(a+b) #addition
print(a-b) #subtraction
print(a*b)#multiplication                         
print(a/b) #division
print(a%b) #modulus
print(a//b) #floor division
print(a**b) #exponentiation

#relational operators
print(a==b) #equal to
print(a!=b) #not equal to
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to

#assignment operators
a=5 #assigning value 5 to variable a
a+=2 #a=a+2                 
print(a)
a*=2 #a=a*2
print(a)
a//=2 #a=a//2
print(a)
a**=2 #a=a**2
print(a)
a%=2 #a=a%2
print(a)

#logical operators
x=True
y=False
print(x and y) #logical and
print(x or y) #logical or 
print(not x) #logical not


# #type conversion(automatic and explicit)
# typecasting(implicit,manual)
a=2
b=3.5
print(a+b) #automatic type conversion

# a="2"
# b=4.5
# print(a+b) #error because a is string and b is float

#typecasting manual
a="2"
b=4.5
a=float(a) #converting string to float
print(a+b) #now it works because a is now a float and b is a float

#can do this
a=3.14
a=str(a) #converting float to string
print(type(a)) #now a is a string

