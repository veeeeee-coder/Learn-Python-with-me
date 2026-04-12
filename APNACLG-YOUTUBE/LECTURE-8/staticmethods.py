#methods that dont use the self parameter(work at class level)

# class Student:
#     @staticmethod  #decorator
#     def college():
#         print("abc clg")

#decorators allow us to wrap another function in order to extend the behaviour of the wrapped function without permanently modifying it

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)


s1 = Student("tony stark", [99, 98, 97])
s1.get_avg()

s1.hello()




# What is @staticmethod

# This is VERY VERY important concept 🚀

# @staticmethod
# def hello():
#     print("hello")

# 👉 Static method means:

# It does NOT use object data

# It does NOT need self

# It behaves like normal function but inside class

# So it is used when:

# ✅ Function is related to class
# ❌ But does not need student name / marks

# Example:

# Greeting message

# College rules

# General info

# Call:

# s1.hello()

# OR even:

# Student.hello()

# Both work.

# Output:
# hello