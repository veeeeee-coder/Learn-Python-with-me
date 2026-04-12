#del keyword-- used to delete object properties or object itself

#del s1.name
#del s1


#private(like) atrr,methods
#private atrr methods are meant to be used only within the class and are not accessible from outside the class
#public-can be accessed everywhere

#to make any attr private add 2 underscores before it
# __acc_pass which makes it private

#only the class inside an internal function can be accessed not outside from it

class Person:
    __name="anoni"

    def __hello(self):
        print("hello veeee!")

    def welcome(self):
        self.__hello()

p1=Person()
print(p1.welcome())
