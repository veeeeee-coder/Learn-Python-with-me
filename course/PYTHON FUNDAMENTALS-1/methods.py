#there are three types of methods in python
#1.instance methods: they are specific to each object of the class. they are defined inside the class and they take self as the first parameter which is a reference to the current object. for example in the class Student we can have an instance method called study() that takes the name of the subject as an argument and prints a message saying that the student is studying that subject. we can call this method using the object of the class Student.
#2.class methods: they are shared by all the objects of the class. they are defined inside the class and they take cls as the first parameter which is a reference to the class. for example in the class Student we can have a class method called get_college_name() that returns the name of the college. we can call this method using the class name or using the object of the class Student.
#3.static methods: they are not specific to any object of the class. they are defined inside the class and they do not take self or cls as the first parameter. for example in the class Student we can have a static method called calculate_cgpa() that takes the marks of the subjects as parameters and returns the cgpa. we can call this method using the class name or using the object of the class Student.

class Laptop:
    storage_type="ssd" #class attribute
    def __init__(self,RAM,storage):
        self.RAM=RAM #instance attribute
        self.storage=storage #instance attribute

    def get_info(self): #instance method
        print(f"RAM: {self.RAM}, Storage: {self.storage}, Storage Type: {self.storage_type}")

l1=Laptop("8gb","512gb") #creating an object of the class Laptop and passing the values for RAM and storage
print(l1.RAM) #accessing the RAM property of the object l1
print(l1.storage) #accessing the storage property of the object l1
print(l1.storage_type) #accessing the storage_type class attribute using the object l1
print(Laptop.storage_type) #accessing the storage_type class attribute using the class name
l1.get_info() #calling the get_info() instance method using the object l1


#this proves that instance method has 1st parameter as self which is a reference to the current object and we can access the properties of the object using self keyword inside the instance method. and we can also access the class attributes using the class name or using the object of the class. (self+access class and instance attributes)




#class method!(first parameter is cls which is a reference to the class and can access class attributes not instance attributes and we can call class method using class name or object of the class and uses @classmethod decorator to define a class method)

class Laptop:
    storage_type="ssd" #class attribute
    def __init__(self,RAM,storage):
        self.RAM=RAM #instance attribute
        self.storage=storage #instance attribute


    @classmethod
    def get_Storage_Type(cls): #class method (class as reference)
        print(f"Storage Type: {cls.storage_type}") #accessing the storage_type class attribute using the cls keyword and here we cant access ram or storage because they are instance attributes and class method can only access class attributes not instance attributes
    def get_info(self): #instance method
        print(f"RAM: {self.RAM}, Storage: {self.storage}, Storage Type: {self.storage_type}")

l1=Laptop("8gb","512gb") #creating an object of the class Laptop and passing the values for RAM and storage
l1.get_Storage_Type() #calling the get_Storage_Type() class method using the object l1
Laptop.get_Storage_Type() #calling the get_Storage_Type() class method using the class name



#static method!(no compulsory parameter not even self or cls) they cannot access class attributes and instance attributes 
#Use it when:
#Function is related to class
#But doesn’t need class or object data
#use @staticmethod decorator to define a static method and we can call static method using class name or object of the class

class Laptop:
    storage_type="ssd" #class attribute
    def __init__(self,RAM,storage):
        self.RAM=RAM #instance attribute
        self.storage=storage #instance attribute

    @staticmethod
    def get_Static_Info(): #static method
        print("This is a static method")

    def get_info(self): #instance method
        print(f"RAM: {self.RAM}, Storage: {self.storage}, Storage Type: {self.storage_type}")

    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(price*discount/100)
        print(f"Final Price after {discount}% discount is: {final_price}")

l1=Laptop("8gb","512gb") #creating an object of the class Laptop and passing the values for RAM and storage
l1.calc_discount(1000,10) #calling the calc_discount() static method using the object l1 and passing the values for price and discount


#problemm
class Product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1

    def get_info(self): #instance method to print the name and price of the product
        print(f"Product Name: {self.name}, Price: {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total number of products: {cls.count}")
    
    @staticmethod
    def calculate_discount(price,discount):
        final_price=price-(price*discount/100)
        print(f"Final Price after {discount}% discount is: {final_price}")

p1=Product("Laptop",1000)
p2=Product("Smartphone",500)
p3=Product("Tablet",300)
p1.get_info()
Product.get_count() 
Product.calculate_discount(1000,10)
p2.calculate_discount(p2.price,10)
