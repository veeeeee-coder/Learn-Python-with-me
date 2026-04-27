#only if a specific condition is true then the code will be executed
#if,elif,else are used for conditional statements

#depending on value of a variable we can execute different blocks of code 

colour=input("enter a colour: ")

if colour=="red":
    print("wait you have to stop")
elif colour=="yellow":
    print("wait you have to get ready")
elif colour=="green":
    print("u can go")

else:
    print("invalid colour")


age=int(input("enter your age:"))
if age<13:
    print("u a child")
elif age>=13 and age<18:
    print("teenagerrr")
elif age>=18:
    print("Adult")


username=input("enter username")
pwd=input("enter pwd")
if username=="admin" and pwd=="pass":
    print("u da real one")
elif username!="admin":
    print("wrong username")
else:
    print("wrong pwd")



#n is multiple of 5 or not 
n=55
if n%5==0:
    print("yeash")
else:
    print("no")


y=int(input("enter a num"))
if y%2==0:
    print("its even")
else:
    print("odd")



#range() function- generates a sequence of numbers
#range(5) -> 0,1,2,3,4
#range(start,stop,step)
#range(1,6) -> 1,2,3,4,5
#range(1,10,2) -> 1,3,5,7,9
