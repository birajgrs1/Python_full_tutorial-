
from abc import ABC, abstractmethod

class ATM(ABC):
    def __init__(self, balance=0):
        self.balance=balance


    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def pin_change(self):
        pass

    def showBalance(self):
        print(f" Your balance is: रु॰{self.balance}")

    def receipt(self):
        print("Receipt printed...")


class simpleATM(ATM):

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -=amount
            print(f"Withdrawal Successful. \n Your new balance: रु॰{self.balance}")

        else:
            print("Insuffient funds!!!")

    def deposit(self, amount):
        self.balance+=amount
        print(f"Deposit Successful. \n New Balance is: रु॰{self.balance}")

    def pin_change(self):
        new_pin = input("Enter your new PIN: ")
        print("PIN change successfully.")
        print(f"Your new PIN is: {new_pin}")


atm=simpleATM(balance=10000)
atm.showBalance()
atm.deposit(2000)
atm.withdraw(3000)
atm.showBalance()
atm.pin_change()
atm.receipt()