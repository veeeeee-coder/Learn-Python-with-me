#strings are a sequence of characters. They are immutable, which means that once a string is created, it cannot be changed.
#strings can be created using single quotes, double quotes, or triple quotes.

word="veee"
print(len(word))
#concatenate
word2="heeeeey"
print(word +" "+ word2)

#indexing meaans position of the character in the string. The first character is at index 0, the second character is at index 1, and so on.
#if len is 6 then 0 to 5 is the index of the characters in the string.

print(word[0])
for ch in word:
    print(ch)

#replacing a character directly is not possible because strings are immutable. But we can create a new string with the desired changes.



#slicing is a way to extract a portion of a string. The syntax for slicing is string[start:end], where start is the index of the first character to include and end is the index of the first character to exclude.gets substring from string from index start to end-1. 
print(word[0:2])
#default start is 0 and default end is len(string)
print(word[:3])
print(word[2:])
print(word[:]) #prints the whole string

#negative indexing means counting from the end of the string. The last character is at index -1, the second to last character is at index -2, and so on.
print(word[-1])
print(word[-3:-1])

#strings formatting-for dynamic strings (diff variables and values)
#1.format method py3 - placeholder is {} and we can pass the values in the format method in the order of the placeholders. placement holder can also have index to specify the position of the value in the format method. we can also use named placeholders and pass the values as keyword arguments in the format method.
a=5
b=10
sum=a+b
#normal formatting
print("the sum of {} and {} is {}".format(a,b,sum)) 
print("language is {}".format("sql"))
#index based formatting
print("the sum of {1} and {0} is {2}".format(a,b,sum))
#value based formatting
print("the sum of {a} and {b} is {c}".format(a=7,b=8,c=15))
#2.f-strings version 3.6 and above - f before the string and the variables are enclosed in curly braces {}. we can also use expressions inside the curly braces.
#literal string interpolation means that we can directly embed expressions inside string literals, using a minimal syntax. The expressions are evaluated at runtime and then formatted using the __format__ protocol.
x=10
y=20
print(f"the sum of {x} and {y} is {x+y}")
print(f"the avg of {x} & {y} is {(x+y)/2}")