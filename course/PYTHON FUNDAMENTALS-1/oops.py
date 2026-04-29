#its the basics of programming
#up until now we have seen procedural programming where we use funtions for code resuability and modularity. but in object oriented programming we use classes and objects to achieve code reusability and modularity. classes are blueprints for creating objects. objects are instances of classes.

#mapping real world objects with code
#object means anything that has state and behavior. for example a car is an object because it has state (color, model, year) and behavior (drive, stop, accelerate). in python we can create a class for the car and then create objects of that class to represent different cars.


#so in a college there are multiple students for each student we have to store numerous amount of information like name adddress dob courses attendance and all up till now we used tuples list dictionaries using that first we create for first student and then copy the same to each and every student (calling every time is an time wasting phenomenon) which is not a good approach as it is not efficient and also it is not a good way to represent the real world objects in code. so we can use classes and objects to represent the students in the college. we can create a class for the student and then create objects of that class to represent different students in the college. this way we can easily store and manage the information of each student in a more organized way.

#class is like a factory where we define a blueprint (predefined) so when storing the information of each student we can create an object of the class and then store the information of each student in that object. this way we can easily manage the information of each student and also we can easily access the information of each student using the object.


#class is blueprint of object, we create class once and object is instance of classs. object takes memory in factories car is the instance of the class and it takes memory in the factory. we can create multiple objects of the same class and each object will have its own state and behavior. for example we can create multiple cars of the same class and each car will have its own color, model, year and behavior.

class Student:
    subject="Python" #class variable
    college="ABC College" #class variable
    year="4th year" #class variable
    def func():
        print("This is a method of the class Student") #method of the class Student

a=10
stu1=Student() #creating an object of the class Student
print(stu1) #<__main__.Student object at 0x7f8c8c8c8c8c> this is the memory address of the object stu1. every time we create an object of the class Student it will have a different memory address.
stu2=Student() #creating another object of the class Student
print(stu2) #<__main__.Student object at 0x7f8c8c8c8c8d> this is the memory address of the object stu2. every time we create an object of the class Student it will have a different memory address.
#use dot operator to access the class variables
print(stu1.subject) #accessing the class variable subject using the object stu1
print(stu2.college) #accessing the class variable college using the object stu2
print(stu1.year) #accessing the class variable year using the object stu1
print(stu2.year) #accessing the class variable year using the object stu2

#observe here that we didnt write the same code for each student to store the information of each student. we created a class for the student and then created objects of that class to represent different students in the college. this way we can easily store and manage the information of each student in a more organized way. this is the main advantage of using classes and objects in python. it helps us to represent real world objects in code and also helps us to manage the information of each object in a more organized way.

#for suppose u want to do it for 3000 student you have to just put it in a loop where we create 3000 objects of the class Student and makeit into list 


#in classes there are two things first is properties which are nothing but variables or attributes that stores information about the object and second is methods which are functions that defines the behavior of the object. for example in the class Student we can have properties like name, age, roll number and methods like study(), attend_class(), etc. methods are used to perform operations on the properties of the object. for example we can have a method called study() that takes the name of the subject as an argument and prints a message saying that the student is studying that subject.


#student-calc_cgpa() and in company we calculate the salary of the employee using a method called calculate_salary() which are behavior of the employee object. so methods are used to define the behavior of the object and properties are used to store the information about the object. this is the main advantage of using classes and objects in python. it helps us to represent real world objects in code and also helps us to manage the information of each object in a more organized way.

#list tuple and all are inbuilt classes
