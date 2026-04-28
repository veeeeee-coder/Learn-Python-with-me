#functions are block of statements that perform a specific task 
#def is used to define a function logic of the function is written inside the function body
#function name should be descriptive of what the function does
#func calls are used to execute the code inside the function invoking a function is called calling a function 
#reusable component of code which can be used multiple times in a program

def hewwo():
    print("hewwo i want to go to coachella")

hewwo() #function call

#arguments->parameters->logic->return value
def add(a,b):#parameters
    sum=a+b
    return sum  #return value is the output of the function which can be used later in the program
result=add(5,10) #function call with arguments
print(result)




def avg(a,b,c):
    averg=(a+b+c)/3
    return averg

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
res=avg(a,b,c)
print("average is", res)


#default parameters- parameters which have default values if no value is passed during function call
def sum(a,b=1):
    return a+b
print(sum(5)) #b takes default value of 1
print(sum(5,10)) #b takes value of 10
#non default parameters should be defined before default parameters in the function definition otherwise it will give an error


#function types- built in functions and user defined functions
#built in functions- functions which are already defined in python and can be used directly without defining them
#user defined functions- functions which are defined by the user to perform a specific task

#lambda functions- anonymous functions which are defined without a name and can be used for short term tasks

lambda_add = lambda a,b,c: a+b+c #lambda function to add three numbers
print(lambda_add(1,2,3)) #function call with arguments

#higher order functions- functions which can take other functions as arguments or return a function as output 

def fact(n):
    f=1
    i=1
    while i<=n:
        f=f*i 
        i+=1
    return f
ans=fact(5)
print(ans)

def calcfactorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(calcfactorial(5))