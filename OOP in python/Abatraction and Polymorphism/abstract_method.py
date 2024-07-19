

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

    def color(self):
        print("Black")

class Maruti_Suzuki(Car):
    def mileage(self):
        print("Mileage is 35kmph")

class TATA(Car):
    def mileage(self):
        print("Mielage is 40Kmph")

# c1=Car()
m1=Maruti_Suzuki()
t1=TATA()
m1.mileage()
t1.mileage()