#only compatible types can be converted to each other
#int to float
#int to bool
#float to int

#two types of type conversion

#1. implicit type conversion- done automatically by python
a=5
b=2.5
c=a+b #5+2.5=7.5
print(c) #7.5
print(type(c)) #<class 'float'>

#when doing division we get a float even if both operands are int it is because of implicit type conversion

#2. (type casting)explicit type conversion- done manually by the programmer using built-in functions
x=10
y=99.8
print(int(y)) #99 loss of data
#to convert x to float
x_float=float(x)
print(x_float) #10.0
print(type(x_float)) #<class 'float'>



#finally
ans1=int(3+63.6)
print(type(ans1),ans1) #<class 'int'> 66

ans2=4+79.8
print(type(ans2),ans2) #<class 'float'> 83.8