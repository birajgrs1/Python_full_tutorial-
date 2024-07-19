

class A:
    _a = 10  # Protected
    __b = 20  # Private

    def show(self):
        print("a=", self._a)
        print("b=", self.__b)

obj = A()
obj.show()  #
print("Outside of class ", A._a)
# print("Outside of class", A.__b)

