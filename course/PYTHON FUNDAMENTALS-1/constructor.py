#constructor is an function to create or construct an object
#1st method __init__ method is a special method in python that is used to initialize the properties of an object. it is called automatically when we create an object of a class. it is also called a constructor because it is used to construct an object. it takes self as the first parameter which is a reference to the current object and then we can take other parameters to initialize the properties of the object. for example in the class Student we can have an __init__ method that takes name, age, roll number as parameters and initializes the properties of the object.
#to initialize our object
#python automatically gets those values from the user when we create an object of the class Student and then it assigns those values to the properties of the object. this is the main advantage of using the __init__ method in python. it helps us to initialize the properties of the object in a more organized way.

#self is the current instance of class,referece to current object or to use properties which is compulsory for all methods it is passed automatically 
class Student:
    def __init__(self): #default constructor
        print("This is the constructor of the class Student") #this is the constructor of the class Student
stu1=Student() #creating an object of the class Student and calling the constructor of the class Student

#jithne bhi objects we create for all that constructor will be called automatically and the message "This is the constructor of the class Student" will be printed for each object that we create. this is the main advantage of using the __init__ method in python. it helps us to initialize the properties of the object in a more organized way and also it helps us to perform some operations when we create an object of the class. for example we can have a method called study() that takes the name of the subject as an argument and prints a message saying that the student is studying that subject. we can call this method inside the __init__ method to print the message when we create an object of the class Student.

#SELF IS PASSED AUTOMATICALLY
class Student:
    def __init__(self,name,cgpa): #parameterized constructor
        self.name=name
        self.cgpa=cgpa

    def get_cgpa(self): 
        return self.cgpa
stu1=Student("John",3.5) #creating an object of the class Student and passing the values for name and cgpa
print(stu1.name) #accessing the name property of the object stu1
print(stu1.get_cgpa()) #accessing the cgpa property of the object stu1
#instance attributes in this are here name and cgpa are instance attributes because they are specific to each object of the class Student. and instance methods are here get_cgpa() is an instance method because it is specific to each object of the class Student. 

#types of constructors
#1.default constructor: it is a constructor that does not take any parameters. it is called automatically when we create an object of a class. it is used to initialize the properties of the object with default values.only has self parameter
#2.parameterized constructor: it is a constructor that takes parameters. it is called automatically when we create an object of a class. it is used to initialize the properties of the object with the values passed as parameters. for example in the class Student we can have a parameterized constructor that takes name and cgpa as parameters and initializes the name and cgpa properties of the object with the values passed as parameters.it has self parameter and other parameters to initialize the properties of the object.

#in python we have only single constructor if multiple it takes the last constructor as the default constructor and the previous constructors will be overridden. one constructor per class
 
#attributes are two types
#1.instance attributes: they are specific to each object of the class. they are defined inside the __init__ method and they are accessed using the self keyword. for example in the class Student we can have instance attributes like name, age, roll number, etc. which are specific to each object of the class Student.(belong to object,unique or different for each object)
#2.class attributes: they are shared by all the objects of the class. they are defined outside the __init__ method and they are accessed using the class name. for example in the class Student we can have class attributes like college name, course name, etc. which are shared by all the objects of the class Student.(belong to class,common)

#name subject cgpa is instance attr college name is class attr

class Student:
    college_name="abc college"
    PI=3.1
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        self.PI=3.14 #instance attribute with same name as class attribute
stu1=Student("John",3.5)
print(stu1.name) #accessing the name property of the object stu1
print(stu1.cgpa) #accessing the cgpa property of the object stu1
print(Student.college_name) #accessing the college_name class attribute using the class name
print(stu1.college_name) #accessing the college_name class attribute using the object stu1
#cannot do this print(Student.name) #raises an error because name is an instance attribute and it cannot be accessed using the class name

#instance attribute has higher priority if they both have same values
print(stu1.PI) #accessing the PI instance attribute of the object stu1 which has higher priority than the PI class attribute
print(Student.PI) #accessing the PI class attribute using the class name which has lower priority than the PI instance attribute of the object stu1