class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def checkbal(self):
        return self.balance


# create object
ba1 = BankAccount(101, "veee", 3900)

# withdraw
ba1.withdraw(1000)

# check balance
print(ba1.checkbal())



class Book:
    def __init__(self, title, author, listofreviews=None):
        self.title = title
        self.author = author
        self.listofreviews = listofreviews if listofreviews else []

    def addreview(self, review):
        self.listofreviews.append(review)

    def countreview(self):
        return len(self.listofreviews)

    def display(self):
        print(self.listofreviews)


# correct object creation
b1 = Book("we do", "veee")

b1.addreview("very good")
b1.addreview("better")

b1.display()
print("Total reviews:", b1.countreview())



class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # ---- Name ----
    def set_name(self, name):
        if name.strip() == "":
            print("Invalid name")
        else:
            self.__name = name

    def get_name(self):
        return self.__name

    # ---- Roll Number ----
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Invalid roll number")

    def get_roll_no(self):
        return self.__roll_no

    # ---- Marks ----
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative")

    def get_marks(self):
        return self.__marks
    
s1 = Student("veee", 25, 90)

print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())


class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    

c = Circle(5)
r = Rectangle(4, 6)

print("Circle area:", c.area())
print("Rectangle area:", r.area())


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats

    def display(self):
        super().display()
        print("Seats:", self.seats)


class Bike(Vehicle):
    def __init__(self, brand, engine_cc):
        super().__init__(brand)
        self.engine_cc = engine_cc

    def display(self):
        super().display()
        print("Engine CC:", self.engine_cc)



from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def calculate_salary(self):
        return 10000


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000


class ContractEmployee(Employee):
    def calculate_salary(self):
        return 30000
    


class Person:
    def __init__(self, name=None, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(self.name, self.age, self.address)

p1 = Person("veee")
p2 = Person("veee", 20)
p3 = Person("veee", 20, "Hyderabad")


class Player:
    player_count = 0   # class variable

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    def display(self):
        print(self.name, self.level)

p1 = Player("A", 1)
p2 = Player("B", 2)

print("Total players:", Player.player_count)



class Herbivore:
    def eat_plants(self):
        print("Eats plants")


class Carnivore:
    def eat_meat(self):
        print("Eats meat")


class Omnivore(Herbivore, Carnivore):
    pass


class Bear(Omnivore):
    def sound(self):
        print("Bear growls")
b = Bear()

b.eat_plants()
b.eat_meat()
b.sound()

