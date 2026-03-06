#slicing-accessing parts of string
#used in machine learning

#str[starting_idx:ending_idx] ending idx is not included 

str="vardhaman college of engineering"
print(str[1:4])
print(str[0:4])
print(str[5:11])
print(str[0:]) #to get till last idx we can also use len(str)
print(str[:4])

#Negative index!!!!
#apple
#-5-4-3-2-1
str1="apple"
print(str1[-3:-1])
print(str1[-5:-1])
#backward counting is helpful when u dont know last character

