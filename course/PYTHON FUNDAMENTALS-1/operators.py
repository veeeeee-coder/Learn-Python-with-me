#to do any operation like in 
#arithmatic we have +,-,*,/,%,**
#assignment operator- =,+=,-=,*=,/=,%=
#comparison operator- ==,!=,>,<,>=,<=
#logical operator- and,or,not
#bitwise operator- &,|,^,~,<<,>>


#arithmatic operator
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# % is modulus operator which gives the remainder of the division
#to get a power b we do a**b    

#relational operator or comarison operator
#gives True or False as output
print(a==b) #if they are equal or not
print(a!=b) #if they are not equal
print(a>b)  #if a is greater than b
print(a<b)  #if a is less than b
print(a>=b) #if a is greater than or equal to b
print(a<=b) #if a is less than or equal to b
#based on the statement we know if its true or false


#assignment operator
c=10
c+=5 #c=c+5
print(c) #15
c-=3 #c=c-3
print(c) #12
c*=2 #c=c*2
print(c) #24
c/=4 #c=c/4
print(c) #6.0
c%=4 #c=c%4
print(c) #2.0

#logical operator
x=True
y=False
print(x and y) #False
print(x or y)  #True
print(not x)   #False
#and- both conditions should be true
#or- at least one condition should be true

#and T,T->T
#and T,F->F
#and F,T->F
#and F,F->F

#OR T,T->T
#or T,F->T
#or F,T->T
#or F,F->F

#opeator precedence
#1. Parentheses ()
#2. Exponentiation **
#3. Multiplication *, Division /, Modulus %
#4. Addition +, Subtraction -
#5. Comparison operators ==, !=, >, <, >=, <=
#6. Logical operators not, and, or

#same precedence operators are evaluated from left to right