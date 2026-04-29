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


students = {}

while True:
    print("\nA: Add Student")
    print("B: Update Marks")
    print("C: Search Student")
    print("D: Display All")
    print("E: Exit")

    choice = input("Enter choice: ").upper()

    if choice == 'A':
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 'B':
        name = input("Enter name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
        else:
            print("Student not found")

    elif choice == 'C':
        name = input("Enter name to search: ")
        if name in students:
            print(name, "marks:", students[name])
        else:
            print("Student not found")

    elif choice == 'D':
        print("All students:")
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == 'E':
        break

    else:
        print("Invalid choice")


words = ["apple", "banana", "kiwi", "cherry", "mango"]

result = {}

for word in words:
    result[word] = len(word)

print(result)




s = input("Enter a string: ")

count = 0
for ch in s:
    if ch == " ":
        count += 1

print("Number of spaces:", count)



list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

s1 = set(list1)
s2 = set(list2)

if s1.isdisjoint(s2):
    print("No common elements")
else:
    print("Common elements exist")



nums = [1, 2, 3, 2, 4, 1, 5]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", list(duplicates))


s = input("Enter a string: ")

unique_chars = set(s)

print("Unique characters:", unique_chars)
print("Count:", len(unique_chars))