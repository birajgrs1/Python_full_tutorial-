
class Vehicle:
    def __init__(self, name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def showDetails(self):
        print(f"Name: {self.name} \n Color: {self.color} \n Model: {self.price} ")

class Car(Vehicle):
    def __init__(self,name,color,price, brand):
        super().__init__(name,color,price)
        self.brand=brand

    def showDetails(self):
        print(f"Name: {self.name} \n Color: {self.color} \n Price: {self.price}  \n Brand: {self.brand}")


# Instance Creation

vech=Vehicle("Generic","White", 3500000 )

car1=Car("SUV", "Black", 4000000, "Toyota" )

# Polymorphism
vech.showDetails()
print("\n------------------------------------\n")
car1.showDetails()

