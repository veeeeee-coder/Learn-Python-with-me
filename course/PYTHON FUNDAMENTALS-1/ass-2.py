salary=int(input("enter salary:"))
if salary <30000:
    ftaxrate=salary-(salary*5)/100
    print(ftaxrate)
elif salary>=30000 and salary<70000:
    ftaxrate=salary-(salary*15)/100
    print(ftaxrate)
elif salary>=70000:
    ftaxrate=salary-(salary*25)/100
    print(ftaxrate)


def eeven(a, b):
    result = []
    if a % 2 != 0:
        a += 1
    for i in range(a, b + 1, 2):
        result.append(i)
    return result


string=input("enter num:")
for numm in string:
    print(numm)



n = int(input("enter num:"))

while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10


wn = int(input("enter num:"))
count=0
while wn > 0:
    digit = wn % 10
    count+=1
    wn = wn // 10
print(count)

n1 = int(input("enter num:"))
sum=0
while n1 > 0:
    digit = n1 % 10
    sum += digit
    n1 = n1 // 10
print(sum)


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


while True:
    user_input = input("Enter a number (or type Quit to stop): ")

    if user_input == "Quit":
        break

    num = int(user_input)

    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")


def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            return "Division by zero not allowed"
        return a / b
    else:
        return "Invalid operation"
    


def isprime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(isprime(5))


secret = 7   # you can choose any number

while True:
    guess = int(input("Guess the number: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        break

