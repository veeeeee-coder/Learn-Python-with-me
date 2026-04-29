#oops pillars
#1. Encapsulation
#2. Inheritance
#3. Polymorphism
#4. Abstraction

#1.Encapsulation- wrapping data and functions into single unit in a class and has data hiding which hides unnecessary details from the user and only shows the necessary details to the user. 
#for example in a bank account we have accid balance name and we have to hide the balance from the user and only show the name and accid to the user. balance is sensitive data only given to private user access

#ACCESS MODIFIERS
#1.public access modifier: it is the default access modifier in python. it allows access to the members of the class from anywhere in the program. for example in the class Student we can have a public attribute called name which can be accessed from anywhere in the program.
#2.private access modifier: it is denoted by double underscore __ before the name of the member. it allows access to the members of the class only within the class. for example in the class Student we can have a private attribute called __roll_number which can only be accessed within the class and cannot be accessed from outside the class.
#3.protected access modifier: it is denoted by a single underscore _ before the name of the member. it allows access to the members of the class within the class and its subclasses. for example in the class Student we can have a protected attribute called _age which can be accessed within the class and its subclasses but cannot be accessed from outside the class.

class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public attribute
        self._balance=balance #protected attribute
        self.__balance=balance #private attribute
    
    def get_balance(self): #getter
        return self.__balance #getter method to access the private attribute __balance
    def set_balance(self,newbalance): #setter  
        self.__balance=newbalance #setter method to set the value of the private attribute __balance

acc1=BankAccount("John",1000) #creating an object of the class BankAccount and passing the values for name and balance
acc1.set_balance(2000) #setting the value of the private attribute __balance using the setter method
print(acc1.name,acc1.get_balance()) 
#in private we have data mangling rather than accessing  with __ we can use getters and setters

#can also do this 
print(acc1._BankAccount__balance) #accessing the private attribute __balance using name mangling but it is not recommended to access private attributes using name mangling because it breaks the encapsulation and it is not a good practice. we should use getters and setters to access private attributes.
















#2.Inheritance - reusing attributes and methods from a parent(base) class (ek class ki properties dusri class use karthi hai) parent class(base) gives to child class (derived class)

class Employee:
    start_time="9am" #class attribute
    end_time="5pm" #class attribute

    def change_shift(self,new_start_time,new_end_time): #instance method
        self.start_time=new_start_time #changing the value of the start_time class attribute using the instance method
        self.end_time=new_end_time #changing the value of the end_time class attribute using the instance method

class Teacher(Employee): #Teacher class is inheriting from Employee class
    def __init__(self,subject):
        self.subject=subject #instance attribute


class Adminstaff(Employee):
    def __init__(self,role):
        self.role=role #instance attribute

class Accountant(Adminstaff):
    def __init__(self,salary,role):
        super().__init__(role) #calling the constructor of the parent class Adminstaff to initialize the role instance attribute
        self.salary=salary #instance attribute

t1=Teacher("Math") #creating an object of the class Teacher and passing the value for subject
t1.change_shift("10am","6pm") #changing the value of the start_time and end_time class attributes using the change_shift() instance method of the Teacher class which is inherited from the Employee class
print(t1.subject,t1.start_time,t1.end_time) #accessing the subject instance attribute and start_time and end_time class attributes using the object t1

a1=Adminstaff("HR") #creating an object of the class Adminstaff and passing the value for role
a1.change_shift("8am","4pm") #changing the value of the start_time and end_time class attributes using the change_shift() instance method of the Adminstaff class which is inherited from the Employee class
print(a1.role,a1.start_time,a1.end_time) #accessing the role instance
acc1=Accountant(50000,"Finance") #creating an object of the class Accountant and passing the values for salary and role
print(acc1.salary,acc1.role,acc1.start_time,acc1.end_time) #accessing the salary and role instance attributes and start_time and end_time class attributes using the object acc1


#types of inheritance

#1.single level inheritance- single parent class and single child class 
#2.multilevel inheritance- single parent class and multiple child classes and one child class is the parent class of another child class
#3.multiple inheritance- multiple parent classes and single child class

class Teacher:
    def __init__(self,salary):
        self.salary=salary #instance attribute
class Student:
    def __init__(self,grade):
        self.grade=grade #instance attribute
class TeachingAssistant(Teacher,Student): #TeachingAssistant class is inheriting from both Teacher and Student classes
    def __init__(self,salary,grade,name):
        Teacher.__init__(self,salary) #calling the constructor of the Teacher class to initialize the salary instance attribute
        Student.__init__(self,grade) #calling the constructor of the Student class to initialize the grade instance attribute here usage of self is compulsory because we are calling the constructor of the parent class and we have to pass the reference to the current object to the constructor of the parent class to initialize the properties of the current object using the constructor of the parent class
        self.name=name #instance attribute

ta1=TeachingAssistant(30000,"A","Alice") #creating an object of the class TeachingAssistant and passing the values for salary, grade and name
print(ta1.salary,ta1.grade,ta1.name) #accessing the salary














#3.abstraction- hiding internal details and showing only essential features to the user. 
#diff between data hiding and abstraction is that data hiding is a part of abstraction. data hiding is the process of hiding the internal details of an object from the user and only showing the necessary details to the user. abstraction is the process of hiding the internal details of an object and only showing the necessary details to the user. abstraction is achieved using abstract classes and abstract methods in python.

#abstract classes are blueprints for other classes. they cannot be instantiated and they are used to define the common interface for the subclasses. abstract methods are methods that are declared in the abstract class but do not have any implementation. the subclasses that inherit from the abstract class must provide an implementation for the abstract methods. this is how abstraction is achieved in python.
#they are part of abc module in python and we have to import abc module to use abstract classes and abstract methods in python. we use @abstractmethod decorator to define an abstract method in the abstract class.

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Lion(Animal):
    def make_sound(self):
        print("roar")


class Cow(Animal):
    def make_sound(self):
        print("moo")

lion=Lion()
lion.make_sound()

cow=Cow()
cow.make_sound()















#4.Polymorphism - many forms(multiple functions(diff forms) same name)
#operator overloading in python + can add and concatenate
#a)Function overriding
#redefining parent class function in child class
#child class overrided the existing parent class function 

class Employee:
    def get_designation(Self):
        print("designation=employee")

class Teacher(Employee):
    def get_designation(Self):
        print("designation=teacher")

t1=Teacher()
t1.get_designation()


#b)duck typing- walks like a duck and quacks like a duck its a duck
class Teacher():
    def get_designation(self):
        print("designation = Teacher")


class Accountant():
    def get_designation(self):
        print("designation = Accountant")


t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()