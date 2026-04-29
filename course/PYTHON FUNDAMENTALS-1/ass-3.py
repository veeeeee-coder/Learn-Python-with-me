user=input("enter a string:")
rev=user[::-1]
if user==rev:
    print("palindrome")
else:
    print("not a palindrome")


#s = input("Enter a string: ")
#rev = ""
#for ch in s:
    #rev = ch + rev   # building reverse
#if s == rev:
    #print("Palindrome")
#else:
    #print("Not a palindrome")

nums = [1, 2, 3, 4, 5]
total = 0

for val in nums:
    total += val

avg = total / len(nums)

print("average:", avg)

list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

merged = list1 + list2   # merging
merged.sort()            # sorting

print("Result:", merged)


t = tuple(map(int, input("Enter tuple elements: ").split()))

even = ()
odd = ()

for num in t:
    if num % 2 == 0:
        even += (num,)
    else:
        odd += (num,)

print("Even tuple:", even)
print("Odd tuple:", odd)


