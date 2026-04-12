# _ _init_ _ function
#Constructor-- all classes have a function called __init__()  which is always executed when the class is being initiated


#the self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class

class Student:

    #default constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self, fullname, marks):
        self.name=fullname
        self.marks=marks
        print("adding new student in database")

s1=Student("veeeee",100)
print(s1.name,s1.marks)

#self can be anything it runs even when its random like abcd we do self becz to avoid confusion


s2=Student("mariyam",0)
print(s2.name,s2.marks)

#name---attributes,variables,data


