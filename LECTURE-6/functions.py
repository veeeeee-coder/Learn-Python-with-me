#block of statements which perform a specific task is called function
#function is a block of code which only runs when it is called
#function is a reusable code


# a=5
# b=10
# sum=a+b
# print(sum)
# #more lines of code

#syntax of function

# def function_name(parameters): #function definition
#     #function body
#     #statements
#     #return statement(optional)

# function_name(arguments) #function call 

#there shudnt be redundant code use function 
#takes input as parameters and gives output

# def summ(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# summ(3,4)
# summ(9,69)


# def print_hewwo():
#     print("hewwwwo")
    
# print_hewwo()
# print(print_hewwo)


#functions are two types built in and user defined


# print("veeclg","veee")#sep=" " automatically adds space between the two strings
# print("geetha")#end="\n" automatically adds new line after the string
# print("geetha",end="")#end="" does not add new line after the string
# print("veee")
# print("geetha",end="$")#end="$" adds $ after the string
# print("veee")


#range(start,end,step) #start is inclusive and end is exclusive

#userdefined function
def cal_prod(a,b):#if not given in arguments give here default values like def cal_prod(a=1,b=1)
    print(a*b)
    return a*b  
cal_prod(3,4)

#giving a at arguments and b at parameters is ok but giving a at parameters and b at arguments is not ok