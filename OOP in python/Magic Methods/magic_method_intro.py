
# __add__ magic method
print("Sum =", (10).__add__(20))


class Bank:
    bank_name="NIC ASIA"
    def __init__(self, acc_no,name,balance):     # __init__ is magic method so no need to call the method
        print("Init is running...")
        self.acc_no=acc_no
        self.name=name
        self.balance=balance

    def __str__(self):
        return self.name


b1=Bank(100, "Ram Dahal", 500000)
print(b1)   #shows string method val
print("Bank Balance is:", b1.balance)

balance = b1.balance + 100000
print("Bank balance now:", balance)

# Using __dict__ attribute
print(b1.__dict__)
print(Bank.__dict__)





# Magic methods and attributes all:

# __init__(self)
class InitDemo:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return f"(a={self.a} , b={self.b})"
id=InitDemo(2,3)
print(id.__dict__)
print(id)  #but these are string now

# __new__ method

class NewDemo:
    def __new__(cls,a,b):
        instance=super().__new__(cls)
        instance.a=a
        instance.b=b
        return instance
nd=NewDemo(3,4)
print(nd.__dict__)






