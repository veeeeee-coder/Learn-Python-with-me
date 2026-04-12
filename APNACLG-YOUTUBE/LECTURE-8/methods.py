#methods are functions that belong to objects

class Student:
    college_name="ABC CLG"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks


s1=Student("veeee",100)
s1.welcome()
print(s1.get_marks())