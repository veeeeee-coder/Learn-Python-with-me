# two types class and instance attributes
# class atrr-same for all(its copied for all objects)
# instance attr-changes

#student(class)---
#s1(name)   s2(name)    s3(name)   
#diff student names for each object so that same way
# self.name tells us that its different for each object we define marks and names for objects
# so these are instance attributes

class Student:
    college_name="vee college"

    # name="anoni" 

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

#here college name is same for all the objects you create for a clg database all students are stores instead of separate storage for each object this represents class attributes

s2=Student("mariyam",0)
print(s2.name,s2.marks)
print(s2.college_name)
print(Student.college_name) #Class attribute!!!


#so s1.name and s1.marks represent objects attributes and Student.college_name represents class attributes

#when we put name={"anoni"} dw it wont print anoni for s1 becuase we already defined name in s1 as veeee so it will print as veee only because of the precendece rules  where    obj attr>class attr!!!!!!!


