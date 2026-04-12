#abstraction--> hiding the implementation deets of a class and only showing essential features to a user


class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")



c = Car()
c.start()


# Driver just sees:
# car started
# He doesn’t care:
# which gear
# clutch timing
# fuel supply
# So the class is hiding complexity




#encapsulation--> wrapping data and functions into single unit(object)
#Encapsulation means wrapping data and methods together in one unit (class) and controlling access to the data.
#Protecting object data from direct outside access

#Think of ATM machine 💳
# Your bank balance = data
# You cannot directly touch the bank server
# You must use:
# withdraw()
# deposit()
# check_balance()
# So:
# 👉 Data is hidden and protected
# 👉 Access happens only through methods
# That is Encapsulation

