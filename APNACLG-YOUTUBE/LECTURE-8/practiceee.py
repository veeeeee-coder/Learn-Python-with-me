class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)


s1 = Student("tony stark", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()





class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)

print(acc1.balance)
print(acc1.account_no)
acc1.credit(2000)
acc1.debit(1500)




