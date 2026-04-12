#when a function calls itself repeatedly until a certain condition is met, it is called recursion.
#recursion is a programming technique where a function calls itself in order to solve a problem.        

#khatarnak version of loop
#recursive function is a function that calls itself in order to solve a problem. It typically has a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
show(5)
#show(5)->show(4)->show(3)->show(2)->show(1)->show(0) and then it will return and print 1,2,3,4,5 in reverse order  when 0 comes vapas chalo vapas chalo hoga
#call stack-when a function is called, it is added to the call stack. When the function returns, it is removed from the call stack. In recursion, each time a function calls itself, a new instance of that function is added to the call stack. This can lead to a large number of function calls and can cause a stack overflow if the recursion is too deep.
#odelete->1(Delete 1)->2(Delete 2)->3(Delete 3)->4(Delete 4)->5(Delete 5) and then it will return and print 5,4,3,2,1 in reverse order when 0 comes 

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

# Execution for fact(5):
# fact(5) → 5 * fact(4)
# fact(4) → 4 * fact(3)
# fact(3) → 3 * fact(2)
# fact(2) → 2 * fact(1)
# fact(1) → 1 (base case)
# Unwind: 2 * 1 = 2, 3 * 2 = 6, 4 * 6 = 24, 5 * 24 = 120
# Output: 120
# This uses the call stack to build the multiplication chain. For large n, it risks stack overflow (like deep loops). An iterative version avoids this.


