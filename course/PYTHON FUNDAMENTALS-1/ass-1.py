username=input("enter your name: ")
age=int(input("enter your age: "))
print("hello", username, "you are", age, "years old!")


num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)


n1=int(input("enter number 1: "))
n2=int(input("enter number 2: "))
f1=float(input("enter float number: "))
n1=float(n1) #type casting- converting int to float
n2=float(n2)
avg=(n1+n2+f1)/3
print("average is", avg)


num_str = input("Enter a number: ")
num_int = int(num_str)
num_float = float(num_str)
num_str_again = str(num_str)

print("Integer:", num_int, "Type:", type(num_int))
print("Float:", num_float, "Type:", type(num_float))
print("String:", num_str_again, "Type:", type(num_str_again))


x=10+3*2**2
print(x) #similar to bodmas but with exponentiation having the highest precedence followed by multiplication and then addition 


a=int(input("enter first number: "))
b=int(input("enter second number: "))
temp=a
a=b
b=temp
print("After swapping: a =", a, "b =", b)


cel=int(input("enter temperature in celsius: "))
cel=float(cel)
fah=(cel*9/5)+32
print("temperature in fahrenheit is", fah)

rad=int(input("enter radius of circle: "))
pi=3.14
area=pi*rad**2
print("area of circle is", area)

principal=int(input("enter principal amount: "))
rate=float(input("enter rate of interest: "))
time=int(input("enter time in years: "))
simple_interest=(principal*rate*time)/100
print("simple interest is", simple_interest)



numf=float(input("enter a float number: "))
numi=int(numf) #type casting- converting float to int
dec=round(numf-numi, 2)
print("integer part is", numi)
print("decimal part is", dec)