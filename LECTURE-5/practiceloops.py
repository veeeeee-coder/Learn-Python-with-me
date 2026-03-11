# #print num from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1


# #print 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1


# #print multiplication table of n
# n=int(input("enter a number"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1


# listt=[8,8,86,4,3,2,1]
# for i in listt:
#     print(i)

# #other
# listt=[8,8,86,4,3,2,1]
# idx=0
# while idx<len(listt):
#     print(listt[idx])
#     idx+=1


nums=[1,2,3,4,5,36,7,8,9,10]
i=0
x=36
while i<len(nums):
    if(nums[i]==x):
        print("found",i)
    else:
        print("finding...")
    i+=1

#break-terminates then and there only,used to terminate the loop when encountered(skips whole loop)
# i=1
# while i<=10:
#     if i==5:
#         break
#     print(i)
#     i+=1   
# print("out of loop")


#continue-terminates execution in current iteration and continues execution of loop w next iteration(skips only one iteration)

i=1
while i<=10:
    if i==5:
        i+=1 #to avoid infinite loop
        continue
    print(i)
    i+=1




i=1
sum=0
while(i<=10):
    sum+=i
    i+=1
print(sum)


i=1
f=1
while i<=5:
    f*=i
    i+=1
print(f)