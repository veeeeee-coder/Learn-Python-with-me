def lennoflistt(listt):
    res=len(listt)
    print(res)
    return res
lennoflistt([1,2,3,4,5])

def ele(listtt):
    for i in (listtt):
        print(i,end=" ")
ele([1,2,3,4,5])


def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
print(fact(5))

def conv(usd):
    inr=usd*82
    
    return inr
print(conv(10))


def oe(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")
oe(7)